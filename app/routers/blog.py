from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# Sample blog post data - in a real application, this would come from a database
blog_posts = [
    {
        "id": 1,
        "title": "Building Explainable AI Systems",
        "summary": "How to make AI systems more transparent and interpretable for end-users.",
        "content": """
        <p>Explainable AI (XAI) is becoming increasingly important as AI systems are deployed in critical domains. This article explores techniques for making AI more interpretable.</p>
        <h3>Why Explainability Matters</h3>
        <p>As AI systems become more complex, the "black box" nature of models like deep neural networks can be problematic, especially in regulated industries or high-stakes decision making.</p>
        <h3>Techniques for Explainable AI</h3>
        <ul>
            <li>LIME (Local Interpretable Model-agnostic Explanations)</li>
            <li>SHAP (SHapley Additive exPlanations)</li>
            <li>Feature importance visualization</li>
            <li>Counterfactual explanations</li>
        </ul>
        <p>By implementing these techniques, we can build AI systems that not only perform well but also provide insights into their decision-making process.</p>
        """,
        "date": datetime(2023, 9, 15),
        "author": "Dr. Data Scientist",
        "tags": ["Explainable AI", "Machine Learning", "Ethics"]
    },
    {
        "id": 2,
        "title": "Optimizing Neural Networks for Production",
        "summary": "Best practices for deploying efficient neural networks in production environments.",
        "content": """
        <p>Neural networks can be resource-intensive. This article shares techniques for optimizing them for production use.</p>
        <h3>The Challenges of Production AI</h3>
        <p>Moving from a research environment to production brings new challenges: latency requirements, resource constraints, and scalability needs.</p>
        <h3>Optimization Techniques</h3>
        <ul>
            <li>Model quantization</li>
            <li>Pruning</li>
            <li>Knowledge distillation</li>
            <li>TensorRT and ONNX conversions</li>
        </ul>
        <p>These approaches can significantly reduce model size and inference time while maintaining accuracy.</p>
        """,
        "date": datetime(2023, 8, 22),
        "author": "Dr. Data Scientist",
        "tags": ["Neural Networks", "Optimization", "MLOps"]
    },
    {
        "id": 3,
        "title": "Ethical Considerations in AI Development",
        "summary": "Exploring the ethical dimensions of artificial intelligence development.",
        "content": """
        <p>As AI becomes more powerful, ethical considerations become increasingly important. This article explores key ethical dimensions of AI development.</p>
        <h3>Key Ethical Dimensions</h3>
        <p>AI ethics encompasses fairness, accountability, transparency, and privacy, among other concerns.</p>
        <h3>Practical Steps</h3>
        <ul>
            <li>Regular bias audits</li>
            <li>Diverse training data</li>
            <li>Stakeholder engagement</li>
            <li>Governance frameworks</li>
        </ul>
        <p>By proactively addressing these ethical dimensions, we can build AI that benefits humanity while minimizing potential harms.</p>
        """,
        "date": datetime(2023, 7, 10),
        "author": "Dr. Data Scientist",
        "tags": ["AI Ethics", "Responsible AI", "Fairness"]
    }
]

@router.get("/", response_class=HTMLResponse)
async def get_blog_posts(request: Request):
    return templates.TemplateResponse(
        "blog.html", 
        {"request": request, "posts": blog_posts, "active_page": "blog"}
    )

@router.get("/{post_id}", response_class=HTMLResponse)
async def get_blog_post(request: Request, post_id: int):
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    if not post:
        return templates.TemplateResponse(
            "404.html", 
            {"request": request}, 
            status_code=404
        )
    return templates.TemplateResponse(
        "blog_post.html", 
        {"request": request, "post": post, "active_page": "blog"}
    ) 