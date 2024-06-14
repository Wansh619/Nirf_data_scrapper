# NIRF Website Data Scraping Project

Welcome to the NIRF Website Data Scraping Project! 🌐

## Overview

This project aims to scrape data from the official NIRF (National Institutional Ranking Framework) website to gather valuable insights into educational institutions' rankings across various categories.

## Features

- **Efficient Scraping:** Utilizing advanced scraping techniques to extract data efficiently from the NIRF website.
- **Customizable Parameters:** Easily customize parameters such as year, category, and institution type for tailored data extraction.
- **Data Parsing:** Structured parsing of scraped data for easy analysis and visualization.
- **Automated Updates:** Scheduled scraping and updating of data to ensure the latest information is available.

## Getting Started

To get started with the project, follow these simple steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/Wansh619/Nirf_data_scrapper.git
   ```
2. **Install Virtual ENV Package:**
   ```
   pip install virtalenv
   ```
3. **Create a New ENV (example_name : env):**
   ```
   virtualenv env
   ```
4. **Start the ENVIRONMENT:**
   ```
   env/Scripts/activate
   ```
5. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```
6. **Run the Scraper:**
   ```
   python main.py
   ```

7. **Explore the Data:**
   Once the scraping is complete, explore the extracted data in the `output` directory.

Note: Use a backward slash when running the code on Powershell and a forward slash when using CmdPrompt.

## External Tool
1. Google Tesseract :
   https://github.com/tesseract-ocr/tesseract
   
## Output Structure
```
OUTPUT
+---College Name
    |   clg_data.json
    |
    +---expenditure
    |       expenditure.csv
    |
    +---parm_image
    |       parms.png
    |
    +---pdf
    |       data.pdf
    |
    +---phd_student
    |       phd_student.csv
    |
    +---sanctioned_intake
    |       sanctioned_intake.csv
    |
    +---total_actual_ss
            total_actual_ss.csv
```
## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue or submit a pull request.

## Acknowledgements

Special thanks to the NIRF website for providing valuable data for analysis.

---

**Happy Scraping!** 🚀




















