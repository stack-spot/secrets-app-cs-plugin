from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess
import json
import os

def put_appsettings(metadata: Metadata, project_name: str, file_name: str):
        os.chdir(f'{metadata.target_path}/src/{project_name}.Api/')
        print(f'Setting {file_name}...')

        with open(file=file_name, encoding='utf-8-sig', mode='r+') as appsettings_json_file:
            appsettings_json_content = json.load(appsettings_json_file)
            appsettings_json_content.update({
                                                "SecretsCache": {
                                                    "CacheItemTTL": metadata.cache_item_ttl,
                                                    "MaxCacheSize": metadata.max_cache_size,
                                                    "VersionStage": f"{metadata.version_stage}",
                                                    "RegionEndpoint": f"{metadata.region_endpoint}"
                                                }                
                                            })                                         
            appsettings_json_file.seek(0)
            json.dump(appsettings_json_content, appsettings_json_file, indent=2)
        print(f'Setting {file_name} done.')   

class Plugin(Template):
    def post_hook(self, metadata: Metadata):
        project_name = metadata.global_inputs['project_name']
        using = f"using StackSpot.Secrets;\n"
        service = f"services.AddSecretsManager(configuration, environment)\n"
        
        put_appsettings(metadata, project_name, 'appsettings.json')
        put_appsettings(metadata, project_name, 'appsettings.Development.json')   

        os.chdir(f'{metadata.target_path}/src/{project_name}.Domain/')
        subprocess.run(['dotnet', 'add', 'package', 'StackSpot.Secrets'])
       
        print('Setting Configuration...')

        os.chdir(f'{metadata.target_path}/src/{project_name}.Api/')
        configuration_file = open(file='ConfigurationStackSpot.cs', mode='r')
        content = configuration_file.readlines()
        index = [x for x in range(len(content)) if 'return services' in content[x].lower()]
        content[0] = using+content[0]
        content[index[0]] = f"{service};\n{content[index[0]]}"
        
        configuration_file = open(file='ConfigurationStackSpot.cs', mode='w')                     
        configuration_file.writelines(content)
        configuration_file.close()

        print('Setting Configuration done.') 

        print('Apply dotnet format...')
        os.chdir(f'{metadata.target_path}/')
        subprocess.run(['dotnet', 'format', './src'])   
        print('Apply dotnet format done...')

if __name__ == '__main__':
    run(Plugin())