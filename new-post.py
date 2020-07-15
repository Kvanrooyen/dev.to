from pathlib import Path
from shutil import copyfile

blog_post_name = input("What is the name of your blog post? \n > ")
blog_post_path = Path("blog-posts", blog_post_name)
blog_post_file = Path(blog_post_path, f'{blog_post_name}.md')
template_file = Path("blog-posts\\template.md")

# Create the post folder
blog_post_path.mkdir(parents=True)

# Create the post file
blog_post_file.touch()

# Copy contents from template.md
copyfile(template_file, blog_post_file)