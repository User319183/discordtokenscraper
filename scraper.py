import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenScraper:
    def __init__(self, file_path):
        self.file_path = file_path

    def scrape_tokens(self):
        tokens = []
        with open(self.file_path, "r+") as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            for line in lines:
                if ":" in line:
                    token = line.split(":")[2].strip()
                    tokens.append(token)
                    f.write(token + "\n")

        logging.info(f"Scraped {len(tokens)} tokens from {self.file_path}")
        return tokens

scraper = TokenScraper("accounts.txt")
tokens = scraper.scrape_tokens()

for token in tokens:
    print(f'{token[:25]}...')
