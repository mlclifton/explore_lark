g = '''
	input_layer=[
		input_neuron={
			id="x1"
		} 
		input_neuron={
			id="x2"
		}
	]
	hidden_layer={
		name="hl1", neurons=[
			perceptron={
				id=1, bias=3,
				input={ id="ipl.1", weight=-2 }
				input={ id="ipl.2", weight=-2 }
			}
		]
	}
	hidden_layer={
		name="hl2", neurons=[
			perceptron={
				id=1, bias=3, 
				input={ id="hl1.1", weight=-2 }
				input={ id="ipl.x1", weight=-2 }
			}
			perceptron={
				id=2, bias=3,
				input={ id="hl1.1", weight=-2 }
				input={ id="ipl.x2", weight=-2 }
			}
		]
	}
	output_layer={
		output_neuron={
			name="sum_bit",
			input={ id=hl2.1, weight=-2 }
			input={ id=hl2.2, weight=-2 }
		}
		output_neuron={
			name="carry_bit"
			input={ id=ol.sum_bit, weight=-2 }
			input={ id=hl1.1, weight=-2 }
		}
	}

'''

nnml_rules = '''
	network: input_layer hidden_layer+ output_layer
	
	input_layer: input_neuron+
	
	input_neuron: "input_neuron" "=" "{" id "}"
	
	id: 
'''

input_fragment = '''
	input_layer=[
		input_neuron={ id="x1" }
		input_neuron={ id="x2" } 
	]

	hidden_layer={
		id="hl2", neurons=[
			perceptron
			perceptron
		]
	}
'''

rule_fragment = '''
	neural_net: input_layer hidden_layer
	
	input_layer: "input_layer" "=" "[" input_neuron+ "]"
	
	input_neuron: "input_neuron" "=" "{" id "}"
	
	hidden_layer: "hidden_layer" "=" "{" id "," "neurons" "=" "[" perceptron+ "]" "}"
	
	perceptron: "perceptron"
	
	id: "id" "=" ESCAPED_STRING

	%import common.ESCAPED_STRING
	%import common.WS
	%ignore WS
'''

from lark import Lark
parser = Lark(rule_fragment, start='input_layer')
op_txt = parser.parse(input_fragment)
print( op_txt.pretty() )

'''
json_parser = Lark(r"""
    value: dict
         | list
         | ESCAPED_STRING
         | SIGNED_NUMBER
         | "true" | "false" | "null"

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')


text = '{"key": ["item0", "item1", 3.14]}'

pt = json_parser.parse(text)
print( pt.pretty() )
'''
