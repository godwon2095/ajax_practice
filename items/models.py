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
    image = models.ImageField(_('대표이미지'), upload_to="image/")
    like_users = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='like_users',
                                        through='Like')
    
    @property
    def likes_count(self):
        return self.like_users.count()


class Like(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_('구매자'), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('상품'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '상품 좋아요'
        verbose_name_plural = '상품 좋아요'
        unique_together = (
            ('user', 'item')
        )


