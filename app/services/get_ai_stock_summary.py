from openai import OpenAI # Assuming you're using the OpenAI client library
from openai import OpenAIError  # For handling OpenAI-specific errors
import json 
import app.core # In case you need to handle JSON parsing
def get_ai_stock_summary(data_string):
    try:
        # Initialize the client with error handling
        try:
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=app.core.api_key,  # Assuming core is properly imported/defined
            )
        except NameError as ne:
            raise NameError("The 'core' module or 'api_key' is not properly defined") from ne
        except Exception as e:
            raise Exception(f"Failed to initialize OpenAI client: {str(e)}") from e

        try:
            # Attempt to create the completion
            print("Data is sent to Ai Model For Summarization")
            completion = client.chat.completions.create(
                extra_body={},
                model="deepseek/deepseek-r1-0528:free",
                messages=[
                    {"role": "system", "content": "You are a stock market analyst. Summarize the trend of the stock over the given period. and generate the reponse in very simpler and short manner"},
                    {"role": "user", "content": f"Stock data: {data_string}"}  # Assuming data_string is defined
                ]
            )
        except OpenAIError as oe:
            raise OpenAIError(f"OpenAI API error: {str(oe)}") from oe
        except KeyError as ke:
            raise KeyError(f"Missing required key in response: {str(ke)}") from ke
        except Exception as e:
            raise Exception(f"Failed to create chat completion: {str(e)}") from e

        try:
            
            print("AI summarization is Completed and info is senting........  to  Subscribers")
            return completion.choices[0].message.content
        except (AttributeError, IndexError) as ae:
            raise ValueError("Unexpected response format from API") from ae
        except Exception as e:
            raise Exception(f"Failed to process API response: {str(e)}") from e

    except NameError as ne:
        print(f"NameError: {str(ne)}")
    except OpenAIError as oe:
        print(f"OpenAI API Error: {str(oe)}")
    except ValueError as ve:
        print(f"Value Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")