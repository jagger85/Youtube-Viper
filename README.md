# Youtube AudioViper -> 🎥 -> 🎧 -> ➡️ -> 📝 -> ➡️ -> 🧠

This app is essentially a "YouTube-to-Insights" pipeline. It downloads audio from YouTube videos, transcribes it into text, and then feeds that transcription into a large language model (LLM) based on a user-provided prompt. Whether you're looking to summarize content, extract key themes, or even ask specific questions about a video, this tool automates the entire process for you.

Think of it as a personal assistant for turning spoken content into actionable insights, it can save time for researchers, content creators, or anyone who wants to quickly analyze YouTube videos without manually watching them.

Use Cases:
- Generate summaries of video content.
- Extract key insights or themes from spoken content.
- Perform sentiment analysis on video transcripts.
- Answer specific questions about the video's content.

To be honest, I didn’t set out to build something scalable at first. I just wanted a tool for myself because I couldn’t find anything quite like it online. But once I started building, I realized how useful this could be for others too. That’s when things got interesting!

**Flask :** I chose Flask because it’s lightweight and easy to work with for APIs. Plus, it gave me the flexibility to iterate quickly.

**Celery + Redis :** As I thought about scaling the app, I knew I’d need to handle long-running tasks like downloading videos and processing transcripts. Celery and Redis became my go-to for managing those jobs asynchronously.

**Docker :** Once I decided to deploy the app, Docker was a no-brainer. It made sure everything ran smoothly across environments—because nobody likes "it works on my machine" issues!

Oh, and fun fact: after my first deployment, I learned the hard way that scraping YouTube might not exactly align with their terms of service (oops! ). So now, instead of hosting it publicly, I’m sharing the codebase here for others to use responsibly. Lesson learned!

Building this project was like my personal playground for experimenting with some cool tech stacks

Orchestrating Flask, Celery, Redis, and Docker : Coordinating all these tools together wasn’t trivial, but it taught me a ton about distributed systems and asynchronous workflows.

Hey, if you’re reading this and thinking, “Wow, this person sounds like they can tackle anything,” then mission accomplished!
## Table of contents

* [Technologies](#technologies)
* [Environment Variables](#environment-variables)
* [Installation](#installation)


## Technologies

<div style="display: flex; gap: 10px;">
<img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask" alt="Flask" />
<img src="https://img.shields.io/badge/Celery-3776AB?style=flat&logo=celery" alt="Celery" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis" alt="Redis" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker" alt="Docker" />
<img src="https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white" alt="Swagger" />
</div>

- **Flask**: A lightweight and flexible Python web framework that powers the API server.

- **Celery**: A distributed task queue system used to handle asynchronous and resource-intensive tasks like video processing and transcription.

- **Redis**: The message broker for Celery, enabling fast and reliable communication between the Flask server and worker nodes. 

- **Docker**: Ensures consistent deployment across environments by packaging the application and its dependencies into portable containers. Docker simplifies development, testing, and production workflows.

- **Swagger**: An open-source tool used to design, document, and test the API endpoints of this project. 

### Additional Tools

- **yt-dlp**: Used for extracting audio from Youtube videos
- **onpenai-whisper**: Used for transcribing the audio to text
- **openai**: Used for proccesing the extracted text
## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:



- **`REDIS_PASSWORD`**: The password for your Redis instance.

- **`MODEL_API_KEY`**: The API key required to authenticate requests to the language model service. Obtain this from the provider of the AI model you're using (e.g., OpenAI or Alibaba Cloud).

- **`MODEL_API_URL`**: The base URL of the language model's API endpoint. This is where the app sends the transcribed text for processing. For example:
  - OpenAI: `https://api.openai.com/v1/chat/completions`
  - Qwen: Check the appropriate endpoint in the Alibaba Cloud documentation.

- **`LLM_MODEL`**: The specific language model to use for processing the transcribed text. Examples include:
  - OpenAI models: `gpt-3.5-turbo`, `gpt-4`.
  - Qwen models: `qwen-plus`, `qwen-max`, or other variants supported by Alibaba Cloud.
  
  > **Note**: This app is compatible with both OpenAI and Qwen LLMs. Ensure you configure the `MODEL_API_KEY` and `MODEL_API_URL` accordingly based on the chosen model.



## Installation

To set up and run this project locally, follow the steps bellow:

**Prerequisites**

Before you begin, ensure you have the docker installed on your machine

1. Start by cloning the project repository on your machine
```bash
git clone https://github.com/jagger85/Youtube-Viper.git
```
2. Set up the environment variables
Navigate to the project folder an create a ```.env``` file.
Refer to [Environment Variables](#environment-variables) section for details on each variable.

3. Build and run the Docker container 
Once the environment variables are configured, build and start the Docker containers using the following command:
```bash
docker compose up --build
```
Once the containers are up and running, the api will be accessible at:
http://127.0.0.1:8000

This address will redirect you to the swagger api documentation,
there you will find a detailed guide to use the api.

🚀 Want a more user-friendly experience? Check out our sleek UI companion app! It provides an intuitive interface for all these features, making video analysis a breeze. Get started at:
https://github.com/jagger85/Youtube-Viper-UI

