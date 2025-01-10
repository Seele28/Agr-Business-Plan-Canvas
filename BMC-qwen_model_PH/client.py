from collections import deque
import dashscope
from process import load_examples
from process import extract_json_content


class Client:
    def __init__(self):
        self.client = None
        dashscope.api_key = "sk-dedc134569de4bc5aa760d2a90146ccc"  # Replace with your actual API key
        self.examples = load_examples()
        self.history = deque([], maxlen=5)

    def chat(self, prompt):
        if len(self.history) == 0:
            _messages = [
                {"role": "system",
                 "content": """You are a professional business consultant with extensive experience in business model development. 
                 When given a business type, generate a comprehensive and detailed BMC that covers all aspects of the business thoroughly.

                 For each component, provide a detailed list of items without any structural notation or JSON objects:

                 - Key Partners: Include all essential partners (suppliers, strategic allies, service providers). Think about direct suppliers, 
                   support services, and strategic partnerships that could enhance the business.

                 - Key Activities: List ALL core activities needed to deliver value, from production to customer service to marketing. 
                   Include both customer-facing and back-office activities.

                 - Key Resources: Consider physical, intellectual, human, and financial resources. Be specific about what's needed 
                   to run the business effectively.

                 - Value Propositions: Detail both tangible and intangible benefits. Include primary and secondary value offerings, 
                   considering different customer segment needs.

                 - Customer Relationships: Describe all ways of interacting with customers, from acquisition to retention to growth.
                   Include both automated and personal relationships.

                 - Channels: List all channels for reaching customers, including marketing, sales, and delivery channels. 
                   Consider both direct and indirect channels.

                 - Customer Segments: Identify all potential customer groups, including primary and secondary segments.
                   Consider both current and potential future segments.

                 - Cost Structure: Include all major and significant minor costs. Consider fixed costs, variable costs, 
                   and economies of scale.

                 - Revenue Streams: List all ways the business makes money, including primary and secondary revenue sources.
                   Consider both one-time and recurring revenue streams.

                 The response must be a clean JSON with these keys: key_partners, key_activities, key_resources, value_propositions,
                 customer_relationships, channels, customer_segments, cost_structure, revenue_streams.
                 Each key should contain a comprehensive array of strings."""},

                {"role": "user",
                 "content": f"Generate a detailed and comprehensive Business Model Canvas for a {prompt} business. Consider all aspects of the business and ensure thorough coverage of each component. Return only the JSON structure.\n\n"
                            f"Example output format:\n"
                            """{"key_partners": ["Dairy suppliers", "Equipment providers"], 
                                "key_activities": ["Manufacturing ice cream", "Managing inventory"]}"""}
            ]
        else:
            _messages = [
                {"role": "system",
                 "content": """You are a professional business consultant helping build a comprehensive BMC.
                 Ensure each component is thoroughly detailed and covers all important aspects of the business.
                 The response must be a clean JSON with each component containing a detailed array of strings."""},

                {"role": "user",
                 "content": prompt + "\nChat history: " + str(list(self.history))}
            ]

        print(_messages)
        response = dashscope.Generation.call(
            model='qwen-turbo',
            messages=_messages,
            max_tokens=2048,
            result_format='message'  # Changed back to 'message' as we'll use extract_json_content
        )

        if not response.status_code == 200:
            raise Exception(f"API call failed with status {response.status_code}")

        if not hasattr(response, 'output') or not response.output:
            raise Exception("No output in response")

        if not hasattr(response.output, 'choices') or not response.output.choices:
            raise Exception("No choices in response")

        content = response.output.choices[0].message.content
        print("Raw response:", content)  # Debug print

        # Extract JSON from the response
        output = extract_json_content(content)
        print("Extracted JSON:", output)  # Debug print

        self.history.append({
            "role": "user",
            "content": output
        })

        self.history.append({
            "role": "bot",
            "content": output
        })
        print(self.history)
        return output