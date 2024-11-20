// generar código que se conecte a la API de OpenWeatherMap.org y obtenga el clima actual de la ciudad que el usuario ingrese js
// Autor: Matronc

// importar librerías
const fetch = require('node-fetch');

// función para obtener el clima
async function clima(ciudad) {
    const api_key = "92d575819c61c039e044b1eea9664027";  // Reemplaza con tu clave de API de OpenWeatherMap
    const base_url = "http://api.openweathermap.org/data/2.5/weather?";
    
    // Construir la URL completa
    const complete_url = `${base_url}q=${ciudad}&appid=${api_key}&units=metric`;
    
    try {
        // Hacer la solicitud a la API
        const response = await fetch(complete_url);
        
        // Convertir la respuesta a JSON
        const x = await response.json();
        
        // Verificar si la respuesta contiene el campo "main"
        if (x.main) {
            const y = x.main;
            const temperatura = y.temp;
            const presion = y.pressure;
            const humedad = y.humidity;
            
            // Obtener la descripción del clima
            const z = x.weather;
            const descripcion_clima = z[0].description;
            
            // Imprimir los resultados
            console.log(`Temperatura: ${temperatura}°C`);
            console.log(`Presión: ${presion} hPa`);
            console.log(`Humedad: ${humedad}%`);
            console.log(`Descripción del clima: ${descripcion_clima}`);
        } else {
            console.log(`Error: No se encontró información del clima para la ciudad ${ciudad}`);
        }
    } catch (error) {
        console.error('Error al obtener el clima:', error);
    }
}

// Entrada de usuario
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Ingrese la ciudad: ', ciudad => {
    // Llamar a la función
    clima(ciudad);
    readline.close();
});