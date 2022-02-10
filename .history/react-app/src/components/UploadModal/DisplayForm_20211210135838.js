import React, { useState, useEffect } from "react";
// import { useSelector } from "react-router-dom";
import { createPost } from "../../store/posts";
import { useDispatch, useSelector } from "react-redux";
import './UploadModal.css'
import logo from './images/instagramme_logo_black.png'

function DisplayForm({ preview, file }) {
    const dispatch = useDispatch();
    const sessionUser = useSelector((state) => state.session.user);
    const user_id = sessionUser.id
    const [description, setDescription] = useState("");
    const [url, setUrl] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        console.log("HANDLE SUBMIT!!!!!")
        e.preventDefault();
        let newErrors = [];
        dispatch(createPost({ user_id, description, file }))
          .then(() => {
            setDescription("");
            setUrl("");
          })
          .catch(async (res) => {
            const data = await res.json();
            if (data && data.errors) {
              newErrors = data.errors;
              setErrors(newErrors);
            }
          });
      };


    return (
        <>
            <div id="post-modal-container">
                <div id="post-modal-image-container">
                    <div id="post-modal-image-wrapper">
                        <div id="inner-div">
                            <img src={preview} alt=""></img>
                        </div>
                        {/* <div id="inner-div-two">Hello from other inner div!</div> */}
                    </div>
                </div>
                <div id="post-modal-right-container">

                    <div id="top-right-container" className="right-column-div">
                        
                    </div>

                </div>
            </div>
        </>
    )
}

export default DisplayForm
