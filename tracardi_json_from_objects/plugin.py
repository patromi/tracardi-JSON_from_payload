from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_json_from_objects.model.models import Configuration
from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_dot_notation.dot_template import DotTemplate


class ConvertAction(ActionRunner):

    def __init__(self, **kwargs):
        self.config = Configuration(**kwargs)

    async def run(self, payload):
        dot = self._get_dot_accessor(payload)
        path = dot[self.config.to_json]

        return Result(port="payload", value={"json": path})


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_json_from_objects.plugin',
            className='ConvertAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={}
        ),
        metadata=MetaData(
            name='tracardi-json-from-objects',
            desc='The purpose of this plugin is convert objects to JSON',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
