pipeline {
    // 1. Agente
    agent any 

    // 1. Declaramos las variables de entorno
    environment {
        // Le decimos a Jenkins que busque la credencial con ID 'discord-webhook-url'
        DISCORD_WEBHOOK = credentials('discord-webhook-url')
    }

    // 2. Etapas
    stages {
        
        // 3. Etapa de Construcción (opcional para Python, pero buena práctica)
        stage('Build') {
            steps {
                echo 'Preparando el entorno...'
                // Si tuvieras dependencias, aquí usarías algo como:
                // bat 'pip install -r requirements.txt'
            }
        }
        
        // 4. Etapa de Pruebas
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                // Ejecuta los tests que creamos antes
                bat 'py -m unittest test_app.py'
            }
        }
        
        // Etapa de Despliegue (Render) - Para más adelante
        stage('Deploy') {
            steps {
                echo 'Aquí irán los pasos para subir a Render'
            }
        }
    }
    
        // 5. Post-acciones (Discord)
    post {
        success {
            echo '¡El pipeline terminó con éxito!'
            // Notificación de éxito a Discord
            bat 'curl -H "Content-Type: application/json" -X POST -d "{\\"content\\": \\" **¡Exito!** El pipeline de pruebas paso correctamente en Jenkins.\\"}" %DISCORD_WEBHOOK%'
        }
        failure {
            echo '¡Hubo un error en el pipeline!'
            // Notificación de error a Discord
            bat 'curl -H "Content-Type: application/json" -X POST -d "{\\"content\\": \\" **¡Error!** El pipeline fallo. Alguien rompio el codigo.\\"}" %DISCORD_WEBHOOK%'
        }
    }
}