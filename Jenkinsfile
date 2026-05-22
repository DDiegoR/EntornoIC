pipeline {
    // 1. Agente
    agent any 

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
                bat 'python -m unittest test_app.py'
            }
        }
        
        // Etapa de Despliegue (Render) - Para más adelante
        stage('Deploy') {
            steps {
                echo 'Aquí irán los pasos para subir a Render'
            }
        }
    }
    
    // 5. Post-acciones (Discord) - Para más adelante
    post {
        success {
            echo '¡El pipeline terminó con éxito!'
            // Aquí iría la notificación de éxito a Discord
        }
        failure {
            echo '¡Hubo un error en el pipeline!'
            // Aquí iría la alerta de fallo a Discord
        }
    }
}