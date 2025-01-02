<<<<<<< HEAD
# Oqila-1
=======
# Oqila - Generative AI Chatbot

Oqila is a generative AI chatbot web application designed to provide users with an interactive experience similar to ChatGPT. The application is built using Python for the backend, Node.js for the server, and React for the frontend, ensuring compatibility across web, desktop, and mobile platforms.

## Project Structure

```
Oqila
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── openai_api
│       └── api_handler.py
├── frontend
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── components
│   │   │   └── Chatbot.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── styles
│   │       └── App.css
│   ├── package.json
│   └── .env
├── mobile
│   ├── App.js
│   ├── index.js
│   ├── components
│   │   └── Chatbot.js
│   ├── styles
│   │   └── App.css
│   └── package.json
├── server
│   ├── server.js
│   ├── package.json
│   └── .env
└── README.md
```

## Features

- **Interactive Chatbot**: Users can interact with the chatbot to generate responses based on their queries.
- **Cross-Platform Compatibility**: The application is designed to work seamlessly on web, desktop, and mobile devices.
- **OpenAI Integration**: Utilizes the OpenAI API to generate responses, ensuring high-quality interactions.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

### Mobile

1. Navigate to the `mobile` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the mobile application:
   ```
   npm start
   ```

### Server

1. Navigate to the `server` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the Node.js server:
   ```
   node server.js
   ```

## Usage

Once the applications are running, users can access the chatbot through the web interface or mobile app. Simply type in your query, and Oqila will generate a response using the OpenAI API.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
>>>>>>> ee9b92ca (Initial commit)
