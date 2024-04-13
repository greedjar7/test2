<script>
    import fastapi from "../lib/api"

    export let params = {}
    let jk_data_id = params.jk_data_id
    
    let jk_data_detail = {}

    function get_jk_detail() {
        fastapi("get", "/api/data/detail/" + jk_data_id, {}, (json) => {
            jk_data_detail = json
        })
    }

    get_jk_detail()
</script>

<h1>{jk_data_detail.company}</h1>
<div>
    {jk_data_detail.title}<br>
    {jk_data_detail.cruit_detail}<br>
    {jk_data_detail.tech_detail}<br>
    {jk_data_detail.link}
</div>