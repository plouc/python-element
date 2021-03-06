import ioc
import os

class Extension(ioc.component.Extension):
    def load(self, config, container_builder):
        path = os.path.dirname(os.path.abspath(__file__))

        loader = ioc.loader.YamlLoader()
        loader.load("%s/resources/config/handler_seo.yml" % path, container_builder)
        loader.load("%s/resources/config/listener_seo.yml" % path, container_builder)


        seo = config.get('seo', {
            'title_pattern': 'Python Element : %s'
        })
        
        container_builder.parameters.set('element.seo.page.title_pattern', seo.get('title_pattern'))
