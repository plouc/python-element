import element.node

class GalleryHandler(element.node.NodeHandler):

    def get_defaults(self, node):
        return {
            'template': 'element.plugins.media:gallery.html'
        }

    def get_name(self):
        return 'Media Gallery'

    def execute(self, context, flask):
        medias = context.node.medias()

        params = {
            'context': context,
            'medias':  medias,
            'lines': [
                [x for x in range(len(medias)) if x - 0 == 0 or ((x - 0) % 4 == 0)],
                [x for x in range(len(medias)) if x - 1 == 0 or ((x - 1) % 4 == 0)],
                [x for x in range(len(medias)) if x - 2 == 0 or ((x - 2) % 4 == 0)],
                [x for x in range(len(medias)) if x - 3 == 0 or ((x - 3) % 4 == 0)],
            ],
        }
        
        return flask.make_response(flask.render_template(context.settings['template'], **params))

class MediaHandler(element.node.NodeHandler):

    def get_defaults(self, node):
        return {
            'template': 'element.plugins.media:media.html'
        }

    def get_name(self):
        return 'Media'

    def execute(self, context, flask):

        params = {
            'context': context,
        }

        return flask.make_response(flask.render_template(context.settings['template'], **params))
