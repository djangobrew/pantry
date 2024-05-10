from dataclasses import dataclass

from django import template
from django.urls import (
    URLPattern,
    URLResolver,
    resolve,
)
from django.utils.html import escape

register = template.Library()


@dataclass
class Breadcrumb:
    name: str = None
    url_pattern: str = None


def normalize_url_name(url_name):
    name = url_name.replace("-", " ").replace("_", " ").title()

    if name.lower().endswith("home"):
        name = name[:-5]

    if name.startswith("Ep"):
        name = name.replace("Ep", "Episode ")

    return name


@register.inclusion_tag("djangobrew/partials/breadcrumbs.html", takes_context=True)
def get_breadcrumbs(context):
    request = context.get("request")
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
            if len(breadcrumbs) == 0 and m.pattern._route != "":
                # ASSUMPTION -- is there a pattern because there is a root url?
                resolver_pattern = url_resolver.pattern._route
                root_url_match = url_resolver.resolve(resolver_pattern)

                # if there was a match for a '' route, meaning there is an app root view
                if root_url_match:
                    breadcrumbs.append(
                        Breadcrumb(
                            name=normalize_url_name(f"{app_name} {root_url_match.url_name}"),
                            url_pattern=f"{app_name}:{root_url_match.url_name}",
                        )
                    )

            # prefix app name, ex. 'Ep02', infront of url name if is app's root url
            breadcrumb_name = f"{app_name} {m.name}" if m.pattern._route == "" else m.name
            b.name = normalize_url_name(breadcrumb_name)
            b.url_pattern = f"{app_name}:{m.name}"
            breadcrumbs.append(b)

    # Add project homepage breadcrumb
    breadcrumbs.insert(0, Breadcrumb(name="Home", url_pattern="root"))

    return {"breadcrumbs": breadcrumbs}


@register.simple_tag(takes_context=True)
def get_app_name(context):
    request = context.get("request")
    app_name = request.resolver_match.app_name

    return normalize_url_name(app_name)


@register.tag(name="code")
def do_code(parser, token):
    nodelist = parser.parse(("endcode",))
    parser.delete_first_token()

    language = "django"

    # TODO: Better kwargs support
    try:
        (_, language) = token.split_contents()

        language = language.split("=")[1]
    except Exception:
        pass

    if language.startswith("'") or language.startswith('"'):
        language = language[1:]
    if language.endswith("'") or language.endswith('"'):
        language = language[:-1]

    return CodeNode(nodelist, language)


class CodeNode(template.Node):
    def __init__(self, nodelist, language="django"):
        self.nodelist = nodelist
        self.language = language

    def render(self, context):
        output = self.nodelist.render(context)

        output = escape(output)

        if output.startswith("\n\n"):
            output = output[2:]
        if output.endswith("\n"):
            output = output[:-1]

        html = f"""
<details class="code-snippet is-clickable">
    <summary>
        <span class="icon-text">
            <span>Show code</span>
            <span class="icon">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-code" width="44"
                    height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <path d="M7 8l-4 4l4 4" />
                    <path d="M17 8l4 4l-4 4" />
                    <path d="M14 4l-4 16" />
                </svg>
            </span>
        </span>
    </summary>

    <pre style="padding: 0;"><code class="language-{self.language}">"""

        html += output
        html += "</code></pre></details>"

        return html
