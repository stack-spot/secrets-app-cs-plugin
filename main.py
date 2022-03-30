from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess
import json
import os

def put_appsettings(metadata: Metadata, target_path: str, file_name: str):
        os.chdir(target_path)
        print(f'Setting {file_name}...')

        with open(file=file_name, encoding='utf-8-sig', mode='r+') as appsettings_json_file:
            appsettings_json_content = json.load(appsettings_json_file)
            appsettings_json_content.update({
                                                "SecretsCache": {
                                                    "CacheItemTTL": metadata.inputs['cache_item_ttl'],
                                                    "MaxCacheSize": metadata.inputs['max_cache_size'],
                                                    "VersionStage": f"{metadata.inputs['version_stage']}",
                                                    "RegionEndpoint": f"{metadata.inputs['region_endpoint']}"
                                                }                
                                            })                                         
            appsettings_json_file.seek(0)
            json.dump(appsettings_json_content, appsettings_json_file, indent=2)
        print(f'Setting {file_name} done.')   

class Plugin(Template):
    def post_hook(self, metadata: Metadata):
        project_name = metadata.global_inputs['project_name']
        using = f"using StackSpot.Secrets;"
        service = f"services.AddSecretsManager(configuration, environment);"
        
        put_appsettings(metadata, f'{metadata.target_path}/src/{project_name}.Api/', 'appsettings.json')
        put_appsettings(metadata, f'{metadata.target_path}/src/{project_name}.Api/', 'appsettings.Development.json')   
        put_appsettings(metadata, f'{metadata.target_path}/tests/{project_name}.Api.IntegrationTests/', 'appsettings.json')

        os.chdir(f'{metadata.target_path}/src/{project_name}.Application/')
        subprocess.run(['dotnet', 'add', 'package', 'StackSpot.Secrets'])

        os.chdir(f'{metadata.target_path}/src/{project_name}.Infrastructure/')
        subprocess.run(['dotnet', 'add', 'package', 'StackSpot.Secrets'])   
       
        print('Setting Configuration...')

        os.chdir(f'{metadata.target_path}/src/{project_name}.Application/Common/StackSpot/')
        configuration_file = open(file='DependencyInjection.cs', mode='r')
        content = configuration_file.readlines()
        index_using = [x for x in range(len(content)) if 'using' in content[x].lower()]
        index = [x for x in range(len(content)) if 'return services' in content[x].lower()]
        content[index_using[0]] = f"{using}\n{content[index_using[0]]}"
        content[index[0]] = f"{service}\n{content[index[0]]}"
        
        configuration_file = open(file='DependencyInjection.cs', mode='w')                     
        configuration_file.writelines(content)
        configuration_file.close()

        print('Setting Configuration done.') 

        print('Apply dotnet format...')
        os.chdir(f'{metadata.target_path}/')
        subprocess.run(['dotnet', 'dotnet-format', f'src/{project_name}.Application/{project_name}.Application.csproj', '--include-generated'])   
        print('Apply dotnet format done...')

if __name__ == '__main__':
    run(Plugin())