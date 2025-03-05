# ArcGPT - Cloud Architecture Diagram Generator

## Overview
ArcGPT is an AI-powered tool that simplifies cloud architecture visualization. By leveraging **Diagrams**, **LangChain**, and **OpenAI**, it enables users to describe their cloud infrastructure in natural language and automatically generate corresponding architecture diagrams. This tool is designed for cloud architects, DevOps engineers, and developers to streamline architecture documentation and visualization.

## Installation Guide (Windows)
Follow these steps to install the required dependencies and set up ArcGPT on your Windows machine.

### **1. Install Python**
Ensure you have **Python 3.8+** installed. If not, download and install it from [Python Official Website](https://www.python.org/downloads/).

### **2. Set Up a Virtual Environment (Optional but Recommended)**
```sh
python -m venv arcgpt-env
arcgpt-env\Scripts\activate
```

### **3. Install Required Libraries**
Run the following commands to install dependencies:
```sh
pip install diagrams langchain openai graphviz streamlit
```

### **4. Install Graphviz (Required for Diagrams Library)**
1. Download Graphviz from: [Graphviz Download](https://graphviz.gitlab.io/download/)
2. Install it and **add the installation path to your system environment variables**.
3. Verify the installation by running:
   ```sh
   dot -V
   ```
   You should see the Graphviz version output.

## Usage
After installing all dependencies, you can start using ArcGPT by running:
```sh
streamlit run Main.py
```

Provide your architecture description, and the system will generate a diagram automatically.

For more information about description follow Example_Description.txt file
## Output

![Architecture Diagram](https://github.com/jaydeepgami56/ArcGPT/blob/main/images/cloud_architecture_1740537171.png)
![Architecture Diagram](https://github.com/jaydeepgami56/ArcGPT/blob/main/images/cloud_architecture_1740537254.png)


## License
ArcGPT is an open-source project. Feel free to contribute!

