import { useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom';
import { getFollowers } from "../../store/followers";
import "./DisplayFollowers.css";

// import { } from '../../store/followers'

function DisplayFollowers({userId, setShowFollowersModal}) {
    // const [isLoaded, setIsLoaded] = useState(false);
    const sessionUser = useSelector((state) => state.session.user);
    const followers = useSelector(state => state.followers);
    const dispatch = useDispatch();
    const history = useHistory();

    useEffect(() => {
        dispatch(getFollowers(userId));
    }, [dispatch, userId]);

    const handleClick = (followerId) => {
        setShowFollowersModal(false);
        history.push(`/users/${followerId}`);
    }

    return (
        <>
            <div className="follows-modal-container">
                <div className='follows-modal-heading'>
                    <div className='follows-modal-heading-text'>Followers</div>
                </div>
                <div className="follows-modal-list">
                    {followers?.map((follower) => {
                        return (
                            <div className="follows-modal-list-row" key={follower.id}>
                                <div className="follows-modal-profile-pic-container">Pic</div>
                                <div className="follows-modal-username"><div className="follows-modal-username-link" onClick={(e) => {handleClick(follower.id)}}>{follower.username}</div></div>
                                <div className="follows-modal-list-button-container">
                                    {sessionUser.id == userId && <button className="follows-modal-remove-button">Remove</button>}
                                    {sessionUser.id != userId && (sessionUser.followers.length === 0 || sessionUser.followers.indexOf(follower.id) == -1) && sessionUser.id != follower.id && <button className="follows-modal-follow-button">Follow</button>}
                                    {sessionUser.id != userId && (sessionUser.followers.indexOf(follower.id) >= 0) && sessionUser.id != follower.id && <button className="follows-modal-following-button">Following</button>}
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>
        </>
    );
}

export default DisplayFollowers;

// // import React, { useEffect } from 'react';
// // import { useSelector } from "react-router-dom";
// import { useSelector, useDispatch } from "react-redux";
// import "./DisplayPost.css";

// import { deletePost } from '../../store/posts'

// import Comment from "../Comments/CommentForm";



// function DisplayPost({ postId, setShowModal }) {
//     const sessionUser = useSelector((state) => state.session.user);
//     const posts = useSelector((state) => state.posts);
//     const post = posts[postId];
//     const dispatch = useDispatch()

//     const handleDelete = (id) => {
//         dispatch(deletePost(id));
//         setShowModal(false);
//     };

//     //   const handleEdit = (id) => {
//     //       dispatch(editPost(id));
//     //   }

//     return (
//         <>
//             <div id="post-modal-container">
//                 <div id="post-modal-image-container">
//                     <div id="post-modal-image-wrapper">
//                         <div id="inner-div">
//                             <img src={post["photos"]} alt=""></img>
//                         </div>
//                     </div>
//                 </div>
//                 <div id="post-modal-right-container">
//                     <div id="top-right-container" className="right-column-div">
//                         <div>
//                             <div id="profile-pic-holder">
//                                 <img id="profile-pic" src={post.profile_image} alt=""></img>
//                             </div>
//                         </div>
//                         <div>{post.username}</div>
//                         <div>
//                             {post.user_id === sessionUser.id && <button>Edit</button>}{" "}
//                             {post.user_id === sessionUser.id && <button onClick={() => handleDelete(postId)}>Delete</button>}
//                         </div>
//                     </div>

//                     <div className='right-column-div' contentEditable='false' >
//                         {post.description}
//                     </div>

//                     <div className="right-column-div">
//                         <Comment post_id={postId} />
//                     </div>
//                     <div className="right-column-div">Button Bar</div>
//                     <div className="right-column-div">
//                         {post.likes} {post.likes === 1 ? "like" : "likes"}
//                     </div>
//                     <div className="right-column-div">New Comment Form</div>
//                 </div>
//             </div>
//         </>
//     );
// }
