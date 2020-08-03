pipeline {
		environment
		{
			registry = "maverick029/digitalnomad"
			registryCredential = 'dockerhub_id'
			dockerImage = 'latest'
		}
		agent any
		stages
		{
			stage('Clone Git')
			{
				steps
				{
					git(credentialsId: '622763aa-a000-40f4-9ebe-fdf1c9568c2f', url: 'https://github.com/maverick029/digitalnomad.git',branch: 'master')
				}
			}
			stage('Building our image')
			{
				steps
				{
					script
					{
						dockerImage = docker.build registry + ":$BUILD_NUMBER"
					}
				}
			}
			stage('Deploy our image')
			{
				steps
				{
					script
					{
						docker.withRegistry( '', registryCredential )
						{
						dockerImage.push()
						}
					}
				}
			}
			stage('Cleaning up')
			{
				steps
				{
					sh "docker rmi $registry:$BUILD_NUMBER"
				}
			}
		}
}