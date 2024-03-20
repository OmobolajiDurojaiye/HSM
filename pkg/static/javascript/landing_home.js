$(document).ready(function(){
    $('#home').click(function(e) {
        e.preventDefault();
        $('#content').html(`
            <div class="search-container">
                <input type="text" id="location" placeholder="Enter location...">
                <button id="search-btn">Search</button>
            </div>
            <div class="filter-options">
                <label for="service-type">Service Type:</label>
                <select id="service-type">
                    <option value="Cleaning & Maintainance">Cleaning & Maintainance</option>
                    <option value="Assembly & Installation">Assembly & Installation</option>
                    <option value="Home Improvement & Repair">Home Improvement & Repair</option>
                </select>
            </div> 

            <div id="serach-container">
                <div class="services">
                    <div class="service-name">
                        <h1>
                            SERVICES
                        </h1>
                    </div>
                    <div class="service-head">
                        <div class="box">
                            <h1>
                                Cleaning & Maintenance
                            </h1>
                        </div>
                        <div class="box">
                            <h1>
                                Home Improvement & Repair
                            </h1>
                        </div>
                        <div class="box">
                            <h1>
                                Assembly & Installation
                            </h1>
                        </div>
                        <div class="box">
                            <h1>
                                Others
                            </h1>
                        </div>
                    </div>
                </div>
            </div>
        `);
    })
})