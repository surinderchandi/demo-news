# Django CMS News Module

A Django CMS extension for creating and managing categorized news articles with flexible display options, multi-author support, and SEO-friendly URLs.

## Project Overview
This project adds a dedicated news module to Django CMS, allowing editors to create, categorize, and display news articles with enhanced features for flexible listings, multi-author support, and a streamlined editorial workflow.

## Features
- **Article Categorization**: Organize articles into categories for easy navigation.
- **Flexible Listings**: Display articles using customizable plugins for editor's picks, category-based listings, and paginated displays.
- **SEO-Friendly URLs**: Article URLs follow an SEO-optimized structure.
- **Multi-Author Support**: Attribute multiple authors to articles.
- **Publication Date Logic**: Shows publication date or "Updated" status based on revisions.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-cms-news-module.git
cd django-cms-news-module


2. Set Up Virtual Environment
python3 -m venv news_demo_env
source news_demo_env/bin/activate

3. Install Dependencies
pip install django djangocms-installer

Usage
Add Categories and Articles: Access Django CMS’s admin interface to create categories and add news articles.
Embed Listings: Use CMS plugins to embed article listings (e.g., Editor’s Picks, category-based lists) on any page.
Customization
Feel free to extend the module by adding additional fields to Article (e.g., tags, featured images) or customizing the cms_plugins.py file to include more listing options.


Contact
For questions, please reach out to ssinder0001@mail.com



This `README.md` provides a comprehensive overview, setup instructions, and guidance on using and customizing the Django CMS news module.
