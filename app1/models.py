from django.db import models

# Predefined Genre model
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensure each genre is unique

    def __str__(self):
        return self.name


class BookOrMovie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, related_name="items", on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    reviewer_name = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(BookOrMovie, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"Review by {self.reviewer_name or 'Anonymous'} - {self.rating} stars"
    
