import datetime
import click


def create_mardown_file(title):
    today = datetime.datetime.now()
    title = title
    date = today.strftime("%Y-%m-%d")
    slug = title.replace(" ", "-").replace(":", "").replace("'", "").strip().lower()
    filename = f"{date}-{slug}"

    content = f"""Title: {title}
Date: {date}
Tags: 
Slug: {slug}
Author: Ricky White
Summary:
Cover:
Status: draft
    """

    with open(f"content/blog/{filename}.md", "w", encoding="utf8") as new_file:
        new_file.writelines(content)

    return print(f"New post created => {filename}")


@click.command()
@click.option(
    "--title",
    prompt="What's the post title?",
    help="Add post title",
    default="untitled",
)
def main(title):
    """Creates the new markdown file with all meta data"""
    create_mardown_file(title)


if __name__ == "__main__":
    main()
