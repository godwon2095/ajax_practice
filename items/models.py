from django.db import models
from users.models import User
from shared.timestamp import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Item(TimeStampedModel):

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = "상품"
        ordering = ['-created_at']

    name = models.CharField(_('상품명'), max_length=200)
    price = models.PositiveIntegerField(_('상품가격'))
    description = models.TextField(_('상품설명'), null=True, blank=True)
    image = models.ImageField(_('상품이미지'), upload_to="image/")
    liked_users = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='liked_users',
                                        through='Like')
    
    def __str__(self):
        return self.name

    @property
    def likes_count(self):
        return self.liked_users.count()

    @property
    def reviews(self):
        return Review.objects.filter(item=self)
        


class Like(TimeStampedModel):

    class Meta:
        verbose_name = '상품 좋아요'
        verbose_name_plural = '상품 좋아요'
        unique_together = (
            ('user', 'item')
        )

    user = models.ForeignKey(User, verbose_name=_('구매자'), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('상품'), on_delete=models.CASCADE)


class Review(TimeStampedModel):

    class Meta:
        verbose_name = '상품 리뷰'
        verbose_name_plural = '상품 리뷰'
        ordering = ['-created_at']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body

