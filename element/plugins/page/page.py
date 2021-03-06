import markdown, os
import element.node
import datetime

class PageHandler(element.node.NodeHandler):
    
    def get_name(self):
        return 'Page'

    def get_defaults(self, node):
        return {
            'template': 'element.plugins.page:default.html'
        }

    def execute(self, context, flask):

        content = context.node.content
        if context.node.format == 'markdown':
            content = markdown.markdown(context.node.content, ['tables'])

        params = {
            'context': context, 
            'content': content,
        }

        return flask.make_response(flask.render_template(context.settings['template'], **params))
