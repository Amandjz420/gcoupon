import csv
import datetime

from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone

from post.models import Post, Tag


class Command(BaseCommand):
    help = 'Create stories'

    def add_arguments(self, parser):

        # Optional argument
        parser.add_argument('-p', '--path', type=str, help='Create stories from the CSV', )

    def handle(self, *args, **kwargs):

        prefix = kwargs['path']
        field_values = {}
        try:
            with open((str(prefix)+'.csv')) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        for field_coutner in range(len(row)):
                            field_values[row[field_coutner]]= field_coutner
                        line_count += 1
                    else:
                        user_id = int(row[field_values['UserId']])
                        post_id = int(row[field_values['PostID']])
                        description = row[field_values['PostDescription']]
                        photo_count = int(row[field_values['photoCount']])
                        tags = row[field_values['Tags']].split(',')
                        tags_to_added = []
                        for tag in tags:
                            tag_obj, created = Tag.objects.get_or_create(
                                name=tag,
                            )
                            tags_to_added.append(tag_obj)
                        images = []
                        if photo_count:
                            for i in range(1, int(photo_count)+1):
                                images.append('https://stpvt-fleek.s3.amazonaws.com/groom%2Fstories%2F'+str(post_id)+'%2F'+str(i)+'.jpg')

                        created_at = datetime.datetime.now(tz=get_current_timezone())
                        modified = datetime.datetime.now(tz=get_current_timezone())

                        if Post.objects.filter(id=post_id).exists():
                            p = Post.objects.get(id=post_id)
                            created_at=p.created_at
                            modified=p.modified

                        p = Post(
                            id=post_id,
                            user_id=user_id,
                            description=description,
                            images=images,
                            type='P',
                            created_at=created_at,
                            modified=modified,
                        )

                        p.save()

                        for tag in tags_to_added:
                            p.tags.add(tag)
                        p.save()
                        line_count += 1

                print(f'Processed {line_count} lines.')
        except Exception as e:
            print(e)
