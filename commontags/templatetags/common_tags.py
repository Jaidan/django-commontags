from itertools import groupby
from django import template

register = template.Library()

@register.tag(name="divide")
def do_division(parser, token):
    try:
        contents = token.split_contents()
        return DivisionResultNode(*contents[1:])
    except:
        raise template.TemplateSyntaxError("Division requires 2 or 3 args")

class DivisionResultNode(template.Node):
    def __init__(self, num, denom, format_string=None):
        self.num = template.Variable(num)
        self.denom = template.Variable(denom)
        self.format_string= template.Variable(format_string)

    def render(self, context):
        num = self.num.resolve(context)
        denom = self.denom.resolve(context)
        format_string = self.format_string.resolve(context)
        try:
            val = float(num) / float(denom)
        except ZeroDivisionError:
            val = 0.0
        if format_string:
            val = format_string.format(val)
        return val

class DynamicRegroupNode(template.Node):
    def __init__(self, target, parser, expression, var_name):
        self.target = target
        self.expression = template.Variable(expression)
        self.var_name = var_name
        self.parser = parser

    def render(self, context):
        obj_list = self.target.resolve(context, True)
        if obj_list == None:
            # target variable wasn't found in context; fail silently.
            context[self.var_name] = []
            return ''
        # List of dictionaries in the format:
        # {'grouper': 'key', 'list': [list of contents]}.

        """
        Try to resolve the filter expression from the template context.
        If the variable doesn't exist, accept the value that passed to the
        template tag and convert it to a string
        """
        try:
            exp = self.expression.resolve(context)
        except template.VariableDoesNotExist:
            exp = str(self.expression)

        filter_exp = self.parser.compile_filter(exp)

        context[self.var_name] = [
            {'grouper': key, 'list': list(val)}
            for key, val in
            groupby(obj_list, lambda v, f=filter_exp.resolve: f(v, True))
        ]
        return ''

@register.tag
def dynamic_regroup(parser, token):
    firstbits = token.contents.split(None, 3)
    if len(firstbits) != 4:
        raise template.TemplateSyntaxError("'regroup' tag takes five arguments")
    target = parser.compile_filter(firstbits[1])
    if firstbits[2] != 'by':
        raise template.TemplateSyntaxError("second argument to 'regroup' tag must be 'by'")
    lastbits_reversed = firstbits[3][::-1].split(None, 2)
    if lastbits_reversed[1][::-1] != 'as':
        raise template.TemplateSyntaxError("next-to-last argument to 'regroup' tag must be 'as'")
    expression = lastbits_reversed[2][::-1]
    var_name = lastbits_reversed[0][::-1]
    return DynamicRegroupNode(target, parser, expression, var_name)
