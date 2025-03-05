import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from diagrams import Diagram
from diagrams.aws.devtools import Codepipeline, Codebuild, Codedeploy
from diagrams.aws.general import General
from langchain_openai import ChatOpenAI
# Set up Streamlit interface
import io,os,glob,time
#set Langchain Smith for the tracing each queries
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]="XXXX"
os.environ["LANGSMITH_PROJECT"]="langchain-academy"

st.title("Cloud Architecture Diagram Generator")
#openai_api_key = st.text_input("Enter your OpenAI API key", type="password")
user_input = st.text_area("Enter your cloud architecture description:")

def generate_diagram_code(description):            
        llm = ChatOpenAI(model="gpt-4o", temperature=0.0, openai_api_key="XXXXXX")
        prompt_template = PromptTemplate(
            input_variables=["description"],
            template = """
Your task is to generate Python code for **{description}** using the **Diagrams** library. Follow these steps strictly:

### **1. Code Output Format**
   - Generate **only executable Python code** with necessary comments.
   - Do **not** include "```" "python", markdown formatting, or extra explanations.**
   - Ensure the generated Python file is **directly runnable**.

### **2. Verify All Imports**
   - Before importing any package, verify its existence from the official **Diagrams** documentation:
     - **AWS Components**: https://diagrams.mingrammer.com/docs/nodes/aws
     - **Azure Components**: https://diagrams.mingrammer.com/docs/nodes/azure
     - **GCP Components**: https://diagrams.mingrammer.com/docs/nodes/gcp
     - **On-Prem Components**: https://diagrams.mingrammer.com/docs/nodes/onprem
     - **Kubernetes Components**: https://diagrams.mingrammer.com/docs/nodes/k8s
     - **Generic Components**: https://diagrams.mingrammer.com/docs/nodes/generic
   - **Do not include incorrect or non-existent imports.**
   - **Handling Missing Services (e.g., MSK)**:
     - If a service **does not exist in the Diagrams library**, do the following:
       1. **Use the closest alternative** (e.g., Kafka from `diagrams.onprem.queue` for MSK).
       2. **If no alternative exists, use a generic component**.
       3. **If a hybrid architecture makes sense, use components from multiple providers**.


### **3. Use the Correct Naming Conventions**
   - Follow proper import syntax based on the provider. Examples:
     - `from diagrams.aws.compute import EC2`
     - `from diagrams.azure.database import DatabaseForPostgresqlServers`
     - `from diagrams.gcp.operations import Monitoring`
     - `from diagrams.onprem.aggregator import Fluentd`
   - If an equivalent service is **not available**, use **a hybrid architecture** by integrating components from multiple providers.

### **4. Code Structure**
   - Use the following structure to generate the diagram:
   from diagrams import Diagram
   # Import necessary components based on the architecture description

   def create_diagram(filename):
       with Diagram("Cloud Architecture", show=False, filename=filename):
           # Define architecture components and their connections
           pass  # Replace with actual diagram logic

   create_diagram("cloud_architecture")
""")
        chain = LLMChain(llm=llm, prompt=prompt_template)
        return chain.run(description)

if st.button("Generate Diagram"):
    if not user_input:
        st.error("Please provide both an API key and a description.")
    else:
        # Set up LangChain
        generated_code=generate_diagram_code(user_input)

        # Display generated code
        st.subheader("Generated Python Code:")
        st.code(generated_code, language="python")
        
        try:
            # Create a unique filename
            timestamp = int(time.time())
            filename = f"cloud_architecture_{timestamp}"
            
            # Modify the generated code to use our filename
            modified_code = generated_code.replace("filename=filename", f"filename='{filename}'")
            # Execute generated code and save diagram
            with io.open("codeGen.py", "w", encoding="utf-8") as f:
                    f.write(modified_code)
            cwd=os.getcwd()
                # Run the script
            os.system("python codeGen.py")
            #exec(modified_code)
                # Display the generated image
            #files = sorted(glob.glob("*.png"), key=os.path.getmtime, reverse=True)
            filename2 = f"{filename}.png"
            if os.path.exists(filename2):
                st.success("Diagram generated successfully!")
                
                st.image(filename2)
            else:
                st.error(f"Diagram file not found: {filename2}")
        except Exception as e:
            st.error(f"Error generating diagram: {str(e)}")
            import traceback
            st.error(traceback.format_exc())