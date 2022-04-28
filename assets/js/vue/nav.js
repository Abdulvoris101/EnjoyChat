var app = new Vue({
    el: '#nav',
    delimiters: ['[[', ']]'],
    data: {
        isMobileMenu: false,
        isCreatedActive: false,
        users: [],
        isSeachModal: false,
        input: '',
        searchActive: true,
        closeActive: false,
        isCloseBtn: false,
        filteredData: []
    },
    created() {
        let url = 'http://localhost:8000/profile/all/list/'
        fetch(url)
            .then(response => response.json())
            .then(data => this.users = data)
            .catch(err => console.log(err.message))
        
    },
    methods: {
        openMobileMenu() {
            this.isMobileMenu = !this.isMobileMenu
        },
        openCreateModal() {
            this.isCreatedActive =  !this.isCreatedActive
        },

        filterUsers() {
            let input = this.input.toLowerCase()
            this.isSeachModal = true
            this.isCloseBtn = true
            this.searchActive = false
            this.filteredData = this.users.filter(username => username['username'].includes(input))
        },
        closeSearchModal() {
            this.input = ''
            this.isSeachModal = false
            this.isCloseBtn = false

            this.searchActive = true
            this.$refs.btn_focus.disabled = true
            this.$refs.btn_focus2.disabled = true
            this.$refs.btn_focus2.disabled = false
            this.$refs.btn_focus2.disabled = false

        }

       
    }
})