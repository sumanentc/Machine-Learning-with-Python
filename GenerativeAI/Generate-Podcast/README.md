## Building an AI generated Podcast

Here we will see, how can we use LLM to generate the contents of an interactive and an engaging Podcast. The topic for the podcast can be any interesting topic from the internet.

![](ai-podcast.jpg)

### Prerequisite
To run this application we will need below API keys.
* OpenAPI Key : [Get OpenAPI key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
* ElevenLabs API Key : [ElevelLabs Key](https://docs.elevenlabs.io/api-reference/quick-start/authentication)

To build this application we will need to perform the below steps.
* Gather Data : To generate any content we will need the data first. Here we will use Wikipedia data to generate the contents. Data can be generated from other sources also.
Here we will use the topic : [Lionel messi](https://en.wikipedia.org/wiki/Lionel_Messi)
* Generate Podcast content: Here we will use LLM-based Text Summarization to generate the Podcast content. We are using OpenAI [gpt-3.5-turbo](https://platform.openai.com/docs/models/gpt-3-5) model for Summarization.
* Generate Podcast Conversation content: Here also, we will use LLM-based model to generate the conversation using the above content. We are using OpenAI [gpt-3.5-turbo](https://platform.openai.com/docs/models/gpt-3-5) model for Podcast conversation generation.
* Generate voice for the podcast conversation: Here we will use [ElevenLabs](https://beta.elevenlabs.io/) to generate custom voice conversation for the podcast.

Sample output for PodCast : [![AI generated Podcast]()](https://github.com/sumanentc/Machine-Learning-with-Python/blob/main/GenerativeAI/Generate-Podcast/podcast.mp4)

Streamlit App : [AI generated Podcast](https://sumanentc-mach-generativeaigenerate-podcaststreamlit-app-b1az6x.streamlit.app/)

### References
* https://beta.elevenlabs.io/
* https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
* https://github.com/openai/openai-cookbook/tree/main
* https://docs.streamlit.io/library/get-started/create-an-app
