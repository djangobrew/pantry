from dataclasses import dataclass

from django import template
from django.conf import settings
from django.urls import (
    get_urlconf,
    get_resolver,
    resolve,
    URLResolver,
    URLPattern,
)

register = template.Library()


@dataclass
class Breadcrumb:
    name: str = None
    url_pattern: str = None


def normalize_url_name(url_name):
    return url_name.replace('-', ' ').replace('_', ' ').title()


@register.inclusion_tag('partials/breadcrumbs.html', takes_context=True)
def get_breadcrumbs(context):
    request = context.get('request')
    match = resolve(request.path)
    last_match = match.tried[-1]
    breadcrumbs = []

    app_name = None
    url_resolver = None
    
    for m in last_match:
        b = Breadcrumb()

        if isinstance(m, URLResolver):
            app_name = m.app_name
            url_resolver = m

        if isinstance(m, URLPattern):

            # add breadcrumb for app's root url if there is one!
            if len(breadcrumbs) == 0 and m.pattern._route != '':

                # ASSUMPTION -- is there a pattern because there is a root url?
                resolver_pattern = url_resolver.pattern._route
                root_url_match = url_resolver.resolve(resolver_pattern)

                # if there was a match for a '' route, meaning there is an app root view
                if root_url_match:
                    breadcrumbs.append(
                        Breadcrumb(
                            name=normalize_url_name(f'{app_name} {root_url_match.url_name}'),
                            url_pattern=f'{app_name}:{root_url_match.url_name}'
                        )   
                    )

            # prefix app name, ex. 'Ep02', infront of url name if is app's root url
            breadcrumb_name = f'{app_name} {m.name}' if m.pattern._route == '' else m.name                
            b.name = normalize_url_name(breadcrumb_name)
            b.url_pattern = f'{app_name}:{m.name}'
            breadcrumbs.append(b)

    # Add project homepage breadcrumb
    breadcrumbs.insert(0, Breadcrumb(name='Home', url_pattern='root'))
    return {'breadcrumbs': breadcrumbs}
