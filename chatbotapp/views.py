
from django.shortcuts import render
from .models import Query
import requests,difflib
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Function to fetch CDP documentation data
def fetch_cdp_data(question):
    urls = {
        "segment": "https://segment.com/docs/connections/sources/catalog/libraries/server/",
        "mparticle": "https://docs.mparticle.com/guides/getting-started/",
        "lytics": "https://docs.lytics.com/docs",
        "zeotap": "https://docs.zeotap.com/home/en-us/"
    }

    best_match = None
    best_score = 0

    # Identify the CDP being asked about
    for cdp, url in urls.items():
        if cdp in question.lower():
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                paragraphs = [p.get_text() for p in soup.find_all("p") if len(p.get_text()) > 30]

                # Find the most relevant paragraph
                for paragraph in paragraphs:
                    score = difflib.SequenceMatcher(None, question.lower(), paragraph.lower()).ratio()
                    if score > best_score:
                        best_score = score
                        best_match = paragraph

                if best_match:
                    return f"Here's what I found for {cdp.title()}:\n\n{best_match}"

            return f"You can read more about {cdp.title()} here: {url}"

    return "I'm sorry, I can only answer questions related to Segment, mParticle, Lytics, and Zeotap."


# API View to handle chatbot queries (store & return JSON response)
@csrf_exempt
def chatbot_query_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))  # ✅ Decode JSON safely
            question = data.get("question", "").strip()

            if not question:
                return JsonResponse({"response": "Please enter a valid question."}, status=400)

            # Fetch response from function
            response_text = fetch_cdp_data(question)

            # Store question & response in the database
            Query.objects.create(question=question, response=response_text)

            return JsonResponse({"response": response_text})  # ✅ Return JSON response

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=405)



# Web Page View
def chatbot_page(request):
    return render(request, "chatbotapp/index.html")
