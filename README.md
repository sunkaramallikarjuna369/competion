# ♿ Accessibility Text Simplifier

**AI-powered tool that makes complex text understandable for everyone**

Built for the AI Product Management Institute Weekend Challenge - A micro-automation tool that removes daily friction by simplifying complex text for people with learning disabilities, non-native speakers, students, and anyone who needs clearer communication.

## 🌟 Why This Tool Matters

Every day, millions of people struggle to understand:
- Legal documents and contracts
- Medical information and prescriptions
- Technical documentation
- Academic papers and textbooks
- Government forms and notices

This tool uses AI to break down complex language into simple, accessible text at three different reading levels, making information accessible to everyone regardless of their reading ability, native language, or learning differences.

## 🎯 Who Benefits?

- **🎓 Students** - Understand complex academic texts and study materials
- **🌍 Non-Native Speakers** - Comprehend documents in their second or third language
- **♿ People with Learning Disabilities** - Access information that would otherwise be too complex (dyslexia, ADHD, etc.)
- **👴 Elderly** - Read legal, medical, and technical documents with clarity
- **⚖️ Legal Document Readers** - Understand contracts, terms, and legal language
- **🏥 Medical Patients** - Comprehend health information and medical instructions

## ✨ Features

- **Multi-Level Simplification**: Choose from 3 reading levels
  - **Basic** (Elementary, Ages 8-10): Very simple words, short sentences
  - **Intermediate** (Middle School, Ages 11-14): Clear everyday language
  - **Advanced** (High School, Ages 15-18): Straightforward, well-structured text

- **Smart Statistics**: See word count reduction and reading level indicators
- **Example Texts**: Try pre-loaded legal, medical, and technical examples
- **Copy to Clipboard**: Easy sharing of simplified text
- **Beautiful UI**: Clean, accessible interface with gradient design

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.12+
- Poetry (Python package manager)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Backend Setup

```bash
cd backend

# Install dependencies
poetry install

# Configure OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Start the backend server
poetry run fastapi dev app/main.py
```

The backend will run on `http://localhost:8000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will run on `http://localhost:4200`

## 📖 How to Use

1. **Paste Your Text**: Copy any complex text into the input area
2. **Choose Reading Level**: Select Basic, Intermediate, or Advanced
3. **Click Simplify**: AI will process and simplify your text
4. **Review Results**: See the simplified version with statistics
5. **Copy & Use**: Copy the simplified text to use anywhere

### Example Use Cases

**Legal Text:**
```
Original: "The party of the first part hereby agrees to indemnify and hold harmless..."
Simplified (Basic): "The first person promises to protect the second person from any problems..."
```

**Medical Text:**
```
Original: "The patient presents with acute myocardial infarction..."
Simplified (Basic): "The patient is having a heart attack..."
```

**Technical Text:**
```
Original: "The algorithm utilizes a convolutional neural network architecture..."
Simplified (Basic): "The computer program uses a special way to learn from pictures..."
```

## 🛠️ Technology Stack

**Backend:**
- FastAPI (Python web framework)
- OpenAI GPT-3.5 Turbo (AI text simplification)
- Python-dotenv (Environment configuration)
- Pydantic (Data validation)

**Frontend:**
- Angular 19 (TypeScript framework)
- CSS3 (Modern styling with gradients)
- HttpClient (API communication)
- FormsModule (Two-way data binding)

## 🔧 API Endpoints

### POST `/api/simplify`
Simplify complex text to a specified reading level.

**Request:**
```json
{
  "text": "Your complex text here",
  "level": "basic"
}
```

**Response:**
```json
{
  "original_text": "...",
  "simplified_text": "...",
  "level": "basic",
  "word_count_original": 50,
  "word_count_simplified": 35,
  "reading_level": "Elementary (Ages 8-10)"
}
```

### GET `/api/stats`
Get API information and available features.

### GET `/healthz`
Health check endpoint.

## 🌐 Deployment

### Backend Deployment (Fly.io)

The backend is deployed using Fly.io:

```bash
# Deploy backend
cd backend
fly deploy
```

### Frontend Deployment

The frontend can be deployed to any static hosting service:

```bash
# Build for production
cd frontend
npm run build

# Deploy the dist/ folder to your hosting service
```

## 💡 How It Works

1. **User Input**: User pastes complex text and selects a reading level
2. **API Request**: Frontend sends text to FastAPI backend
3. **AI Processing**: Backend uses OpenAI GPT-3.5 to simplify text with specific prompts for each reading level
4. **Response**: Simplified text is returned with statistics
5. **Display**: Frontend shows results with word count comparison and reading level

### AI Prompts

Each reading level uses carefully crafted prompts:

- **Basic**: Uses very simple words (≤2 syllables), short sentences (5-10 words), no jargon
- **Intermediate**: Uses everyday words, medium sentences (10-15 words), explains technical terms
- **Advanced**: Uses clear language, well-structured sentences, maintains accuracy

## 🔒 Security & Privacy

- API keys are stored securely in `.env` files (never committed to git)
- CORS is configured for secure cross-origin requests
- No user data is stored or logged
- All text processing happens in real-time

## 📊 Impact & Use Cases

**Education:**
- Teachers can simplify complex materials for students
- Students can understand difficult textbooks and papers

**Healthcare:**
- Patients can understand medical instructions
- Caregivers can explain health information to elderly patients

**Legal:**
- Citizens can understand contracts and legal documents
- Non-lawyers can comprehend terms and conditions

**Business:**
- Companies can make documentation accessible
- Customer service can simplify complex explanations

**Government:**
- Public services can make forms and notices understandable
- Information can reach all citizens regardless of reading level

## 🎨 Design Philosophy

The tool follows accessibility-first design principles:

- **High Contrast**: Easy-to-read text with clear visual hierarchy
- **Large Touch Targets**: Buttons are easy to click/tap
- **Clear Labels**: Every element is clearly labeled
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Emoji Icons**: Universal symbols for quick recognition
- **Gradient Design**: Modern, engaging visual appeal

## 🚧 Future Enhancements

- [ ] Support for multiple languages
- [ ] Batch processing of multiple documents
- [ ] PDF upload and processing
- [ ] Browser extension for on-the-fly simplification
- [ ] Save and share simplified texts
- [ ] Audio reading of simplified text (text-to-speech)
- [ ] Customizable reading levels
- [ ] Integration with learning management systems

## 📝 License

This project is open source and available for educational and personal use.

## 👨‍💻 Author

Built with ❤️ by @sunkaramallikarjuna369 for the AI Product Management Institute Weekend Challenge

## 🙏 Acknowledgments

- OpenAI for GPT-3.5 Turbo API
- Angular team for the amazing framework
- FastAPI for the elegant Python web framework
- AI Product Management Institute for the challenge

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**One-liner:** AI-powered text simplifier that makes complex documents accessible to everyone - from legal jargon to medical terms, simplified in seconds! 🚀
