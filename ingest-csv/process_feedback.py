import csv
import json
from ai import chain
import concurrent.futures

from text_processing import is_valid_string

def process_feedback(df, output_path):

    # Ingest a single row
    def process_row(i, row):
        new_row = [i] + row.to_list()
        text = row["text"]

        if is_valid_string(str(text)):
            try:
                res = json.loads(chain.run(feedback=text))
                sentiment = res["sentiment"]
                topics = ", ".join(res["topics"])
            except:
                sentiment = "NA"
                topics = "NA"
        else:
            sentiment = "NA"
            topics = "NA"

        new_row.extend([sentiment, topics])
        return new_row

    with open(output_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            # Submit tasks to thread pool
            futures = [executor.submit(process_row, i, row) for i, row in df.iterrows()]
            
            # Collect results as they become available
            for future in concurrent.futures.as_completed(futures):
                new_row = future.result()
                writer.writerow(new_row)
    