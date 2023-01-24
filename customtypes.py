from typing import TypedDict, Literal
CharacterTypes = TypedDict('CharacterTypes', {'uppercase': bool, 'lowercase': bool, 'digits': bool, 'symbols': bool})
OptionType = Literal['uppercase', 'lowerase', 'digits', 'symbols']