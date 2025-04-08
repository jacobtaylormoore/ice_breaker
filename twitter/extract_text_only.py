import json
import os

def extract_tweet_data(input_filepath="C:\Users\jacob\coding\ai\ice_breaker\twitter\combined_data.json", output_filepath="C:\Users\jacob\coding\ai\ice_breaker\twitter\results\text_only.json", limit=0, include_date: bool = True):
    """
    Extracts 'text', 'createdAt' (optional), and 'url' from each tweet in a JSON file
    and saves the extracted data to a new JSON file.

    Args:
        input_filepath: Path to the input JSON file.
        output_filepath: Path to the output JSON file.
        include_date: included by default
    """
    try:
        with open(input_filepath, 'r') as infile:
            data = json.load(infile)
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_filepath}")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in: {input_filepath}")
        return

    extracted_data = []

    if isinstance(data, list):
        tweet_count = 0
        for item in data:
            if limit:
                if tweet_count >= limit:
                    break
            if isinstance(item, dict) and item.get("type") == "tweet":  # Check if it's a tweet
                # Use .get() to safely access keys, handle missing keys gracefully
                text = item.get("text")
                created_at = item.get("createdAt")
                url = item.get("url")

                # Create a dictionary only if all required fields exist
                if text is not None and created_at is not None and url is not None:
                    # Decide on including date
                    if include_date:
                        extracted_data.append({
                            "text": text,
                            "createdAt": created_at,
                            "url": url
                        })
                    else:
                        extracted_data.append({
                            "text": text,
                            "url": url
                        })
                    tweet_count += 1
                else:
                     print(f"Warning: Skipping item due to missing 'text', 'createdAt', or 'url': {item}")

            elif isinstance(item, dict):
                print(f"Warning: Skipping dictionary (not a tweet): {item}")
            else:
                 print(f"Warning: Skipping item of unexpected type {type(item)}: {item}")

    elif isinstance(data, dict):  # Handle case if input is a single dictionary
          print("Warning: Input file contains a dictionary, not a list of tweets.")
          if data.get("type") == "tweet": #check if dict is a tweet
            text = data.get("text")
            created_at = data.get("createdAt")
            url = data.get("url")
            if text is not None and created_at is not None and url is not None:
                extracted_data.append({
                    "text": text,
                    "createdAt": created_at,
                    "url": url
                })
            else:
                print(f"Warning: Skipping item due to missing 'text', 'createdAt', or 'url': {data}")


    else:
        print(f"Error: Input file contains unexpected data type: {type(data)}")
        return

    # Save the extracted data
    try:
        with open(output_filepath, 'w') as outfile:
            json.dump(extracted_data, outfile, indent=4)
        print(f"Extracted data saved to: {output_filepath}")
        return json.dumps(extracted_data, indent=4)
        
    except Exception as e:
        print(f"Error writing to output file: {e}")



def main():
    """Main function to handle file selection and processing."""
    input_directory = "./results/bo_tweets"  # Or wherever your combined JSON file is
    input_filename = "combined_data.json"  # Or whatever you named the combined file
    input_filepath = os.path.join(input_directory, input_filename)

    output_directory = "./results/bo_tweets"  # Or a different output directory if you prefer
    output_filename = "extracted_tweet_data.json"
    output_filepath = os.path.join(output_directory, output_filename)

    # Ensure output directory exists
    if not os.path.exists(output_directory):
      os.makedirs(output_directory)

    extract_tweet_data(input_filepath, output_filepath)

if __name__ == "__main__":
    main()