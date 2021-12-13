import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import "./post.css";
import DisplayPostModal from "../User";
import like_empty from './images/likes.png'
import liked from './images/likes_filled_red.png'
import comment from './images/comment.png'
import { addLike } from "../../store/likes";

const Post = ({
  id,
  user_id,
  description,
  username,
  likes,
  comments,
  photos,
  profile_image,
}) => {

  const dispatch = useDispatch();

const like = (id) => {
  dispatch(addLike(id))
};

  return (
    <div className="post-box">
      <div className="user">
        <img className="profile-image-post" src={profile_image} />
        <NavLink className="username_link" to={`/users/${user_id}`}>
          {username}
        </NavLink>
      </div>
      <div className="photo-holder">
        <img className="photo"
        src={photos} alt="post-photo" />
      </div>
      <div className="description">{description}</div>
      <div className="post-icons">
      {likes.find((like) =>)}
      <img src={like_empty} className="like-icon"></img>
      <img src={comment} className="comment-icon"></img>
      </div>
      <div className="likes">{likes} likes</div>
      <div className="comments">{comments} comments</div>
    </div>
  );
};

export default Post;