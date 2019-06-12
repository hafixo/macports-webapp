from django import template
register = template.Library()


@register.simple_tag
def build_url(builder_name, build_id):
    return "https://build.macports.org/builders/ports-" + builder_name + "-builder/builds/" + str(build_id)


@register.simple_tag
def watcher_url(builder_name, watcher_id):
    return "https://build.macports.org/builders/ports-" + builder_name + "-watcher/builds/" + str(watcher_id)
