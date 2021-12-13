import { useSelector, useDispatch } from "react-redux";
import { useEffect } from 'react';
import { useHistory } from "react-router-dom";
import { getFollowing, resetFollowing } from "../../store/following";
import './FollowingFeed.css'


function FollowingFeed () {
  const dispatch = useDispatch();
  const history = useHistory();
  const sessionUser = useSelector((state) => state.session.user);
  const following = useSelector(state => state.following);
  const userId = sessionUser.id

  useEffect(() => {
    dispatch(getFollowing(userId));
  }, [dispatch, userId]);

  const handleClick = (followeeId) => {
    dispatch(resetFollowing());
    history.push(`/users/${followeeId}`);
  }
    return (

      <div className="following-feed-container">
       {following?.map((followee) => {
                        return (
                          <div className="following-feed-tile" key={followee.id}>
                            <div className="following-feed-pic-container"><img className="following-feed-profile-pic" src={followee.profile_image} alt="" onClick={() => { handleClick(followee.id) }}></img>
                                </div>
                                <div className="following-feed-username">
                                  <div className="following-feed-username-link" onClick={() => { handleClick(followee.id) }}>{followee.username}
                                  </div>
                              </div>
                            </div>
                        )
                    })}
      </div>
    )
 }

 export default FollowingFeed
