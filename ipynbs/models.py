from django.db import models

# Create your models here.


class TestMode(models.Model):
    # db_column is used to change the column name in database and access that as name
    # editable=False is used to make field not editable from form

    name = models.CharField(max_length=255,
                            db_column="user_name",
                            db_index=True)
    description = models.TextField(db_column="user_desc",
                                   blank=True,
                                   null=True,
                                   help_text="Description of the test mode")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # abstract = True # donot create table for this table use it for inheritance
        app_label = 'core'  # app is registered under which registered app
        db_table = "test_mode"  # table name where data to be stored
        get_latest_by = "created_at"  # get latest data by which field
        ordering = ("created_at", )  # order by which field
        unique_together = ("name", "description")  # unique together
        permissions = (("can_read", "Can read"), )  # permission
        verbose_name = "Test Mode"  # verbose name
