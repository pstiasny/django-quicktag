# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Template, Context

class SampleTagTest(TestCase):

    def assertRenderEquals(self, tag_code, expected, context=None):
        t = Template("{% load dummyapp_tags %}" + tag_code)
        content = t.render(Context(context or {}))
        self.assertEquals(content, expected)

    def test_tag_with_no_args_prints_nothing(self):
        self.assertRenderEquals("{% sampletag %}", '')

    def test_tag_with_single_arg_prints_arg(self):
        self.assertRenderEquals("{% sampletag 'yo' %}", "Args: yo")

    def test_tag_with_multiple_args_prints_arg_list(self):
        self.assertRenderEquals("{% sampletag 'yo','hey' %}", "Args: yo, hey")
        # Vary spacing around comma
        self.assertRenderEquals("{% sampletag 'yo', 'hey' %}", "Args: yo, hey")
        self.assertRenderEquals("{% sampletag 'yo' ,'hey' %}", "Args: yo, hey")
        self.assertRenderEquals("{% sampletag 'yo' , 'hey' %}", "Args: yo, hey")

    def test_tag_with_single_kwarg_prints_keyword_and_value(self):
        self.assertRenderEquals("{% sampletag kw1='yo' %}", "Kwargs: kw1=yo")

    def test_tag_with_multiple_kwargs_prints_a_keyword_and_value_list(self):
        self.assertRenderEquals("{% sampletag kw1='yo',kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")
        # Vary spacing around comma
        self.assertRenderEquals("{% sampletag kw1='yo', kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")
        self.assertRenderEquals("{% sampletag kw1='yo' ,kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")
        self.assertRenderEquals("{% sampletag kw1='yo' , kw2='hey' %}", "Kwargs: kw1=yo, kw2=hey")

    def test_tag_with_context_prints_keyword_and_value_list(self):
        self.assertRenderEquals("{% sampletag_withcontext %}",
                                "Context: myvar=yo", context={'myvar': 'yo'})

    def test_tag_prints_filtered_arg(self):
        self.assertRenderEquals("{% sampletag 'yo'|upper %}", "Args: YO")

    def test_tag_prints_filtered_kwarg(self):
        self.assertRenderEquals("{% sampletag kw1='yo'|upper %}", "Kwargs: kw1=YO")

    def test_tag_prints_variable_arg(self):
        self.assertRenderEquals("{% sampletag myvar %}", "Args: yo", context={'myvar': 'yo'})

    def test_tag_prints_variable_kwarg(self):
        self.assertRenderEquals("{% sampletag kw1=myvar %}", "Kwargs: kw1=yo", context={'myvar': 'yo'})

    def test_tag_with_space_in_arg(self):
        self.assertRenderEquals("{% sampletag 'yo hey' %}", "Args: yo hey")

