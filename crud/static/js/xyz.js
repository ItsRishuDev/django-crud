const deleteConfirm = (id) =>{
    // Delete Confirmation
    var ask = confirm('Are you sure to delete employee');
    // if sure 
    if (ask && id) {
        // calling delete 
        window.location.href = "/delete/"+id;
    } else {
    }
    return false;
}
