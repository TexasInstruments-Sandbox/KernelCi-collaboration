import yaml
from jsonschema import validate, ValidationError

# Load schema
schema = yaml.safe_load(open('../hardware_registry_schema.yaml'))
data_dict  = yaml.safe_load(open('../hardware_registry.yaml'))

try:
    validate(instance=data_dict, schema=schema)
    print("? Validation successful � corrected dataset conforms to schema!")
    print(f"Silicon vendors: {len(data_dict['silicon_vendors'])}")
    print(f"Processors: {len(data_dict['processors'])}")
    print(f"Platform vendors: {len(data_dict['platform_vendors'])}")
    if 'system_modules' in data_dict:
        print(f"System modules: {len(data_dict['system_modules'])}")
    print(f"platforms: {len(data_dict['platforms'])}")
except ValidationError as e:
    print("? Validation error:")
    print(f"   Message: {e.message}")
    print(f"   Path: {' -> '.join(map(str,e.path))}")
    print(f"   Schema path: {' -> '.join(map(str,e.schema_path))}")