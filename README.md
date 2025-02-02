### **Legal Document Analyzer: Project Summary**

**Objective:**  
To create a FastAPI-based application capable of analyzing legal documents by allowing users to upload files (PDFs/Word documents), extracting their text, and performing basic Natural Language Processing (NLP) analysis.

---

### **Key Features:**

1. **File Upload Endpoint**  
   - Users can upload legal documents through an API endpoint.
   - Supported file formats: PDF and Word (.docx).
   - The API saves the file locally and extracts its text.

2. **Text Extraction**  
   - Uses libraries like PyPDF2 (for PDFs) and python-docx (for Word documents).
   - Handles file parsing to retrieve plain text for further analysis.

3. **NLP Analysis**  
   - Implements NLP techniques to analyze the extracted text:
     - **Word Frequency Analysis:** Identifies the most common words.
     - **Named Entity Recognition (NER):** Extracts entities like names, dates, and locations using `spaCy`.
     - **Key Phrases:** Extracts meaningful phrases from the text.

4. **Database Integration**  
   - Stores metadata of uploaded files and analysis results in a MySQL database.
   - SQLAlchemy is used for ORM (Object Relational Mapping).

5. **Swagger Documentation**  
   - The API is fully documented using Swagger UI.
   - Provides a user-friendly interface for testing endpoints.

6. **Error Handling**  
   - Handles common issues like unsupported file formats, file parsing errors, and database connection issues gracefully.

---

### **Technologies Used:**

- **Backend Framework:** FastAPI
- **Database:** MySQL
- **NLP Libraries:** spaCy
- **File Handling:** PyPDF2, python-docx
- **Environment:** Python virtual environment
- **Deployment:** Uvicorn (development server)

---

### **Workflow:**

1. **User uploads a document via Swagger UI or a client app.**
2. **Text is extracted from the document.**
3. **NLP analysis is performed on the extracted text.**
4. **Results (e.g., named entities, word frequency) are returned to the user as JSON.**
5. **Metadata and results are saved in the database for future reference.**
