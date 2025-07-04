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
                    {"role": "system", "content": "
                    🧠 Role: You are a seasoned stock market analyst with 30+ years of deep expertise in macroeconomics, domestic and global equity markets.
                    📩 Input:
                    I’ll give you a single data point in the format:
                    Index Name | Current Price | Change (points) | Change (%)
                    Example: NIFTY 50 25,461.00 55.70 (0.22%) or NASDAQ 17,920.20 -148.50 (-0.82%).

                    🎯 Task:
                    Analyze the index performance and generate a short 3-bullet-point snapshot in basic English with appropriate emojis for clarity.

                    📌 Output Format:

                    📊 Market Movement Summary:
                    Mention whether the index moved 📈 up, 📉 down, or ➖ flat. State the movement in points and percentage, with a tone that matches the magnitude (e.g., modest, sharp, slight).

                    🔍 Key Drivers Behind the Move (3 detailed points):

                    Highlight macro or micro triggers (e.g., FII/DII activity, interest rates, crude oil movement, currency, corporate earnings, geopolitical tensions).

                    Mention specific sectors or events driving the move.

                    Use real insights — not placeholders like "global cues" unless necessary — and avoid vague phrases.

                    👨‍💼 What It Means for Retail Investors:
                    One simple sentence telling the likely short-term outlook or guidance. Keep it easy to follow — for example:
                    ✅ "Hold your positions."
                    ⚠️ "Be cautious near resistance zones."
                    💡 "Buying opportunity if you're a long-term investor."

                    🚫 Do NOT include:

                    Generic endings like “Ready for next data point!”

                    Phrases like “Likely impact on India” if it's a global index — just integrate impact insight into the main bullets if needed.
                     "},
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
