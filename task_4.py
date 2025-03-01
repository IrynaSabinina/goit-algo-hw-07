class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Adds a reply to the current comment."""
        self.replies.append(reply)

    def remove_reply(self):
        """Marks the comment as deleted but keeps replies intact."""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        """Recursively displays the comment and its replies in a hierarchical structure."""
        prefix = '    ' * indent  # Indentation for hierarchy
        if self.is_deleted:
            print(f"{prefix}{self.text}")  # Display as deleted
        else:
            print(f"{prefix}{self.author}: {self.text}")  # Display author and comment
        
        for reply in self.replies:
            reply.display(indent + 1)  # Recursively display replies with indentation

# Example Usage
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Remove a comment (mark it as deleted)
reply1.remove_reply()

# Display all comments with hierarchy
root_comment.display()
