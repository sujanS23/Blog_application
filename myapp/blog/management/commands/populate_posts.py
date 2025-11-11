from typing import Any
from blog.models import Post,Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args, **options):
        # Deleting Exising data 
        Post.objects.all().delete()
        
        titles = [
    "The Future of AI",
    "Climate Change Solutions",
    "Remote Work Trends",
    "Quantum Computing Explained",
    "Renewable Energy Innovations",
    "Deep Learning Demystified",
    "Post-Pandemic Economic Outlook",
    "Blockchain in Finance",
    "Storytelling in Marketing",
    "Medical Technology Advances",
    "Space Exploration Challenges",
    "Psychology of Decision Making",
    "Evolution of Social Media",
    "The Art of Cooking",
    "Cultural Diversity in Society",
    "Sustainable Development Investments",
    "Globalization Impact",
    "Power of Mindfulness",
    "Online Learning Revolution",
    "Art and Technology Fusion",
]

        contents = [
    "Exploring the future of artificial intelligence and its profound impact on society, businesses, and everyday human life.",
    "Discovering innovative solutions to combat climate change and protect the environment for future generations to thrive.",
    "Analyzing the latest trends, opportunities, and challenges in remote and hybrid work environments across industries.",
    "An introduction to the principles, applications, and transformative potential of quantum computing in modern technology.",
    "Investigating groundbreaking innovations in renewable energy sources to build a more sustainable and greener planet.",
    "Understanding the fundamentals, architectures, and real-world applications of deep learning and neural networks.",
    "Examining the global economic landscape and business recovery strategies in the aftermath of the COVID-19 pandemic.",
    "Exploring the transformative potential of blockchain technology in revolutionizing the financial and banking sector.",
    "Harnessing the power of storytelling, creativity, and digital strategies to design compelling marketing campaigns.",
    "Highlighting groundbreaking breakthroughs, cutting-edge tools, and advancements in modern medical technology.",
    "Addressing the obstacles, risks, and exciting opportunities in the ever-expanding domain of space exploration.",
    "Exploring the psychological and emotional factors that influence human behavior and decision-making processes.",
    "Tracing the evolution of social media platforms and analyzing their long-term impact on communication and society.",
    "Celebrating the art of cooking, culinary creativity, and the cultural significance of food in bringing people together.",
    "Promoting inclusivity, embracing diversity, and building stronger modern communities through unity and respect.",
    "Investigating global sustainable development initiatives and their measurable impact on shaping the future world.",
    "Examining the effects of globalization on both local markets and the interconnected global economies of today.",
    "Embracing mindfulness practices, meditation techniques, and mental strategies for enhanced well-being and productivity.",
    "Revolutionizing modern education through digital learning platforms, online resources, and virtual collaboration tools.",
    "Exploring the intersection of art, design, and technology to create inspiring innovations in the digital age.",
]


        img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",
]

        categories=Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls) :
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))