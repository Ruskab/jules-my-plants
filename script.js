const plantsData = [
    // ... (plant data as defined in the previous step) ...
    {
        name: "Fiddle Leaf Fig", // Name matches mockup
        scientificName: "Ficus lyrata", // Example scientific name
        emoji: "🌳",
        imagePlaceholder: "Imagen de Fiddle Leaf Fig",
        imageUrl: "https://lh3.googleusercontent.com/aida-public/AB6AXuD69R8CyZPxc_TVEjSxc5sPzc2b6Kj_Uwvk2IPuzn4ERxRFUepVxaXC1FnR2ZG1_Qnq0eFPEBV4C-UCHz3gjlPgbY9rZKDelDshFoiq9XN5d3DGSbhi9_MbkDyzvz5oTiJoaX3fFBLyL_S_AT9T3y1hqJdqkgEjPZi0gUU-sHgu_XtwboKbLLGSM1g4fvcRKO5E53aj_AIfMriMXRVtlHLyxKxUu60xhkjh4PSWNxH07Qo60cA13HbWCIry4dAu79xmu5y2HyFOkdZv",
        watering: "Top 2-3 cm dry", // Corresponds to "Water when"
        checkFrequency: "7-10 days", // Corresponds to "Check every"
        tip: "Loves bright, indirect light."
    },
    {
        name: "Snake Plant", // Name matches mockup
        scientificName: "Sansevieria trifasciata",
        emoji: "🐍",
        imagePlaceholder: "Imagen de Snake Plant",
        imageUrl: "https://lh3.googleusercontent.com/aida-public/AB6AXuBxF6ufV57JxhMcMD8Yg-_ZNKEjkVF0pCFWws-QzxKnf-fwUC2PqMl1BOgjlvJFQpUXH1TVUBGf6yfwQrY2Botxzs1MP7gkyttLgMbqULNS7rYoTIaDY3QnQStjCAo3ierfX6iqJ8Q9hPtqIs_LDjd5bRvxFiI4PWFbHAnaHT3qHi9loeW1-kn2cM2egsy-FvqzZ1r9itY1_dB4kt3p-0iQ31dSmOXk-qsjKNM9-fphaNFnOvvwnWDiMEhcUyU0cCL5PcxHn1v5RbWh",
        watering: "Soil completely dry",
        checkFrequency: "14-28 days",
        tip: "Very drought tolerant."
    },
    {
        name: "Peace Lily", // Name matches mockup
        scientificName: "Spathiphyllum wallisii",
        emoji: "🕊️",
        imagePlaceholder: "Imagen de Peace Lily",
        imageUrl: "https://lh3.googleusercontent.com/aida-public/AB6AXuAS9iJ1nZhy7AK0D9Y12Q-j73OlCy1pqJH9B0PnSNEyO-CCk3FbpuCuinvzpwHh6Xa2mqjiBBlKj-N5xWF2B7BNyEFE6AUOrPnD7aMjHXbz5wkbYe1OALf8wmh6Wjvhm2Z-ORJ4Kxq_JcqgiFIQIz-nD8_x6-edFLvjYUHFHHiDJv8s1KcQAuUnUISJx01yEjcI6XWQvyXL3wmIjOQ7irovALqVKdftuV5ZfHltV7LaCmmEyI38TIzhjJ60h73lRpM3MwYVWIBVONiL",
        watering: "Top 2.5 cm dry",
        checkFrequency: "5-7 days",
        tip: "Prefers filtered water."
    },
    {
        name: "Monstera", // Name matches mockup
        scientificName: "Monstera deliciosa",
        emoji: "🌿",
        imagePlaceholder: "Imagen de Monstera",
        imageUrl: "https://lh3.googleusercontent.com/aida-public/AB6AXuD2Q7G_qv47fu0C4PtOlRxvNM8TXKw859bZefl3wvvR9XXNWGzxSjk58t3rVpxxHEVNG8f1KmGxQe4WOpQJa3cWTUp_e0kv0QMS69LxoethGRBS-dAIBGHMC70vOs4PJ1szqgwyTltIJkANJVVsZBOHff7h-hYSD8p5eQPC6N7O8Hmnou2ntauGihlyjfgX-Vob7BAkZwWgd-dje1lMRXjBm5VEONuMAb8oAyXSjvb23eDdBrpDMPCZ0oL-yhZ8xGTpxssb96sQFdSG",
        watering: "Top 5 cm dry",
        checkFrequency: "7-14 days",
        tip: "Loves humidity, mist occasionally."
    },
    {
        name: "ZZ Plant", // Name matches mockup
        scientificName: "Zamioculcas zamiifolia",
        emoji: "💰",
        imagePlaceholder: "Imagen de ZZ Plant",
        imageUrl: "https://lh3.googleusercontent.com/aida-public/AB6AXuCgxccFaX5vR_X2obcvrNf2q4nUY2UqWj2ME_NyBMsCjvvsqcFCBwfVAkCSujl6770eLOgqpRIJJrQJQVufEKfaOmQHYl30YOq-wchTufkYXy5uHH65e67yv4rBreFolNtCRYJ20mC3qkenVFQZq-bNX0GB6A_cfaw_Hz5pJxffqCO2GP0nwTXRE6jD-J7m9rWoquPZsPls1jEzYti7CK8DSmyuTjuktWlctt8aGiP3g3DRYutPzrMdg0MeFAn3UEjVaNlxW_emzMzI",
        watering: "Soil completely dry",
        checkFrequency: "21-28 days",
        tip: "Tolerates low light."
    },
    {
        name: "Calathea", // Name matches mockup
        scientificName: "Calathea ornata", // Example, could be any Calathea
        emoji: "🎨",
        imagePlaceholder: "Imagen de Calathea",
        imageUrl: "https://lh3.googleusercontent.com/aida-public/AB6AXuAzn0mrozxgKJQd6S4nMgvtGBtzAsCwAbefAB_xpAnKJTOsSrHcMk-rDQC0RojFhk1yFTl4es0mcDh2OdoMc99rqGAQTK-ODt_2jqzLLolALZpfTvSdfDpX8wGm65TpDgf8_okWJhJ-Si9Gj_AqdwACcl-Hg2QvWRMte90T6PFm3hPmr1h12pt4TfOLkn8-0zvS_OhWvXUweXcb2fBFoVtmldJ0K6kLPfDERO2P00BhUiQI84wHLcUNmuGK6mzwjDx72PuR9iyYyNNo",
        watering: "Top 2-3 cm dry",
        checkFrequency: "3-5 days",
        tip: "High humidity needs."
    },
    // Original data from the second HTML - these will go to "Upcoming" by default for now
    {
        name: "Potho Neón",
        scientificName: "Epipremnum aureum 'Neon'",
        emoji: "🪴",
        imagePlaceholder: "Imagen de Potho Neón",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Potho+Neón",
        watering: "Cuando los 2-5 cm superiores del sustrato estén secos.",
        checkFrequency: "3-5 días (con 25.7°C).",
        tip: "Prefiere quedarse un poco corto de agua que pasarse. Hojas lacias pueden ser señal de sed."
    },
    {
        name: "Palmera de Salón",
        scientificName: "Chamaedorea elegans",
        emoji: "🌴",
        imagePlaceholder: "Imagen de Palmera de Salón",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Palmera+Salón",
        watering: "Cuando los 2-3 cm superiores del sustrato estén secos.",
        checkFrequency: "4-7 días (más cerca de 4-5 días con calor).",
        tip: "Sensible al exceso de agua. La humedad ambiental actual le gusta."
    },
    {
        name: "Dracaena",
        scientificName: "Dracaena fragrans - Tronco de Brasil",
        emoji: "🌱",
        imagePlaceholder: "Imagen de Dracaena",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Dracaena",
        watering: "Cuando los primeros 5 cm (o 1/3 de la maceta) estén bien secos.",
        checkFrequency: "7-14 días (más cerca de 7-10 días con calor).",
        tip: "Muy tolerante a la sequía. ¡No la ahogues! Agua reposada o filtrada es mejor."
    },
    {
        name: "Calathea zebrina", // This is a duplicate name, but different scientific name.
                                // The categorization logic should handle it, perhaps placing it in default.
        scientificName: "Goeppertia zebrina",
        emoji: "🦓",
        imagePlaceholder: "Imagen de Calathea zebrina",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Calathea",
        watering: "Cuando el centímetro superior del sustrato comience a secarse. Mantener húmedo, no empapado.",
        checkFrequency: "2-4 días (necesita atención frecuente con calor).",
        tip: "¡Ama la humedad! El 66.8% es genial. Agua filtrada o de lluvia es ideal."
    },
    {
        name: "Yuca",
        scientificName: "Yucca elephantipes",
        emoji: "🌵",
        imagePlaceholder: "Imagen de Yuca",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Yuca",
        watering: "Cuando la mayor parte del sustrato esté seco. Muy tolerante a la sequía.",
        checkFrequency: "10-20 días (o más si está a pleno sol).",
        tip: "El exceso de riego es su enemigo. Drenaje excelente es crucial."
    },
    {
        name: "Palmera Areca",
        scientificName: "Chrysalidocarpus lutescens",
        emoji: "🌞",
        imagePlaceholder: "Imagen de Palmera Areca",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Palmera+Areca",
        watering: "Cuando los 2-4 cm superiores del sustrato estén secos.",
        checkFrequency: "4-7 días.",
        tip: "Le gusta la humedad ambiental. Evita que se seque por completo."
    },
    {
        name: "Poto Dorado Colgante",
        scientificName: "Epipremnum aureum",
        emoji: "✨",
        imagePlaceholder: "Imagen de Poto Dorado Colgante",
        imageUrl: "https://placehold.co/600x400/A7F3D0/166534?text=Poto+Colgante",
        watering: "Cuando los 2-5 cm superiores del sustrato estén secos.",
        checkFrequency: "5-10 días.",
        tip: "Muy resistente. Similar al Potho Neón, mejor pecar de seco que de húmedo."
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const upcomingPlantsGrid = document.querySelector('#upcoming-plants .grid');
    const needsWateringPlantsGrid = document.querySelector('#needs-watering-plants .grid');
    const overduePlantsGrid = document.querySelector('#overdue-plants .grid');

    // Ensure grids exist
    if (!upcomingPlantsGrid || !needsWateringPlantsGrid || !overduePlantsGrid) {
        console.error("One or more plant grids not found!");
        return;
    }

    function createPlantCard(plant, category) {
        const card = document.createElement('div');
        card.className = 'plant-card group'; // Added group class for hover effects

        const imageWrapper = document.createElement('div');
        imageWrapper.className = 'plant-image-wrapper';

        const img = document.createElement('img');
        img.src = plant.imageUrl || 'https://placehold.co/300x300/e2e8f0/94a3b8?text=' + encodeURIComponent(plant.imagePlaceholder || 'Plant Image');
        img.alt = plant.name;
        img.className = 'plant-image';
        img.onerror = function() {
            this.src = 'https://placehold.co/300x300/e2e8f0/94a3b8?text=' + encodeURIComponent(plant.imagePlaceholder || 'Error Loading');
        };

        const statusIndicator = document.createElement('div');
        statusIndicator.className = 'plant-status-indicator'; // Base class
        const statusIcon = document.createElement('span');
        statusIcon.className = 'material-icons-outlined text-sm';

        let wateringStatusText = '';

        // Category-specific setup
        if (category === 'Upcoming') {
            statusIndicator.classList.add('bg-green-500');
            statusIcon.textContent = 'schedule';
            if (plant.name === "Fiddle Leaf Fig") wateringStatusText = "Water in 2 days";
            else if (plant.name === "Snake Plant") wateringStatusText = "Water in 3 days";
            else if (plant.name === "Peace Lily") wateringStatusText = "Water in 4 days";
            else wateringStatusText = "Water soon"; // Default for other upcoming
        } else if (category === 'Needs Watering') {
            statusIndicator.classList.add('bg-orange-500');
            statusIcon.textContent = 'opacity';
            wateringStatusText = "Water today";
        } else if (category === 'Overdue') {
            statusIndicator.classList.add('bg-red-500');
            statusIcon.textContent = 'warning_amber';
            if (plant.name === "Calathea") wateringStatusText = "Water 2 days ago";
            else wateringStatusText = "Overdue"; // Default for other overdue
        } else { // Default/fallback if category is somehow not set
            statusIndicator.classList.add('bg-gray-400');
            statusIcon.textContent = 'help_outline';
            wateringStatusText = "Status unknown";
        }

        statusIndicator.appendChild(statusIcon);
        imageWrapper.appendChild(img);
        imageWrapper.appendChild(statusIndicator);

        const info = document.createElement('div');
        info.className = 'plant-info';

        const nameP = document.createElement('p');
        nameP.className = 'plant-name';
        nameP.textContent = plant.name;

        const wateringStatusP = document.createElement('p');
        wateringStatusP.className = 'plant-watering-status';
        // Set color based on category
        if (category === 'Upcoming') wateringStatusP.classList.add('text-green-600');
        else if (category === 'Needs Watering') wateringStatusP.classList.add('text-orange-600');
        else if (category === 'Overdue') wateringStatusP.classList.add('text-red-600');
        else wateringStatusP.classList.add('text-gray-600');

        const statusDot = document.createElement('span');
        statusDot.className = 'status-dot';
        if (category === 'Upcoming') statusDot.classList.add('bg-green-500');
        else if (category === 'Needs Watering') statusDot.classList.add('bg-orange-500');
        else if (category === 'Overdue') statusDot.classList.add('bg-red-500');
        else statusDot.classList.add('bg-gray-500');
        
        wateringStatusP.appendChild(statusDot);
        wateringStatusP.appendChild(document.createTextNode(wateringStatusText));

        const instructionsDiv = document.createElement('div');
        instructionsDiv.className = 'watering-instructions';
        
        const waterWhenP = document.createElement('p');
        const waterWhenLabel = document.createElement('span');
        waterWhenLabel.className = 'instruction-label';
        waterWhenLabel.textContent = 'Water when: ';
        waterWhenP.appendChild(waterWhenLabel);
        waterWhenP.appendChild(document.createTextNode(plant.watering || 'N/A')); // Use plant.watering here

        const checkEveryP = document.createElement('p');
        const checkEveryLabel = document.createElement('span');
        checkEveryLabel.className = 'instruction-label';
        checkEveryLabel.textContent = 'Check every: ';
        checkEveryP.appendChild(checkEveryLabel);
        checkEveryP.appendChild(document.createTextNode(plant.checkFrequency || 'N/A')); // Use plant.checkFrequency here

        instructionsDiv.appendChild(waterWhenP);
        instructionsDiv.appendChild(checkEveryP);

        // Optional: Add tip if it exists and you want to display it
        if (plant.tip) {
            const tipP = document.createElement('p');
            tipP.className = 'text-xs text-slate-500 mt-1'; // Simple styling for tip
            tipP.innerHTML = `<span class="instruction-label">Tip:</span> ${plant.tip}`;
            instructionsDiv.appendChild(tipP);
        }

        info.appendChild(nameP);
        info.appendChild(wateringStatusP);
        info.appendChild(instructionsDiv);

        card.appendChild(imageWrapper);
        card.appendChild(info);

        return card;
    }

    plantsData.forEach(plant => {
        let category = 'Upcoming'; // Default category
        let targetGrid = upcomingPlantsGrid;

        // Categorization logic based on names from the mockup
        if (plant.name === "Fiddle Leaf Fig" || plant.name === "Snake Plant" || plant.name === "Peace Lily") {
            category = 'Upcoming';
            targetGrid = upcomingPlantsGrid;
        } else if (plant.name === "Monstera" || plant.name === "ZZ Plant") {
            category = 'Needs Watering';
            targetGrid = needsWateringPlantsGrid;
        } else if (plant.name === "Calathea") { // Catches "Calathea" from mockup data
            category = 'Overdue';
            targetGrid = overduePlantsGrid;
        } else {
            // For other plants from the merged data, assign them to 'Upcoming' for now
            // This part can be refined if more specific rules are needed for the plants from the second HTML.
            // For example, the "Calathea zebrina" will fall here.
            category = 'Upcoming';
            targetGrid = upcomingPlantsGrid;
        }
        
        const plantCard = createPlantCard(plant, category);
        targetGrid.appendChild(plantCard);
    });
    console.log('Plant cards generated and added to the DOM.');
});
