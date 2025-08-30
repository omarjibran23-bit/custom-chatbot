Python Chatbot That Learns from You
This is a terminal-based Python chatbot that learns from a single block of text input. Users can copy and paste any paragraph, essay, or mixed-format content (including questions, statements, or dialogue), and the bot will extract question-answer pairs to build its knowledge base.
Features
• 	Accepts one block of text containing mixed types such as questions, statements, and dialogue
• 	Automatically extracts question-answer pairs from the input
• 	Answers user questions based on learned content
• 	Suggests similar questions using fuzzy matching
• 	Allows manual teaching when no match is found
• 	Saves and loads memory using a JSON file
• 	Tracks skipped sentences and allows retrying learning
Requirements
• 	Python 3.x
• 	No external libraries required
How to Use
1. 	Copy the entire chatbot code into a file named chatbot.py
2. 	Open a terminal in the folder containing chatbot.py
3. 	Run the chatbot using:
3. 	python chatbot.py
4. 	Use the following commands to interact:
4. 	learn - Paste a block of text (can include different sentence types) for the bot to learn from
learn-list - View all learned question-answer pairs
/learn-1,2,3 - View questions, answers, or both from the last input
/learn-skip - View sentences that were skipped during learning
/learn-skip-1,2,3,... - Retry learning from selected skipped sentences
save - Save current memory to memory.json
exit - Quit the chatbot
Use Cases
• 	Educational tool for learning basic NLP concepts
• 	Practice building chatbots with Python
• 	Explore text parsing and pattern recognition
• 	Useful for students, hobbyists, and educators
Credits
Developed by Jibran
Assisted by Copilot
